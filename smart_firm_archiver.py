import os
import re
from typing import Annotated, TypedDict
from dotenv import load_dotenv

from langchain.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import SystemMessage

system_message = SystemMessage(content=(
    "You are a financial assistant. "
    "1. Use 'get_project_info' to find budgets. "
    "2. Use 'calculate_tax' ONLY ONCE to get the final total. "
    "3. Once you have the final taxed amount, provide the final answer immediately. "
    "4. DO NOT call 'calculate_tax' on an amount that already includes tax."
))

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
path = "Level_6/smart_firm_archiver_Langgraph/data"

def setup_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name= "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    loader = DirectoryLoader (path, glob= "*.txt", loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"})
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    for doc in split_docs:
        budget = re.search (r"(\d+)\s*USD", doc.page_content)
        if budget:
            price = int(budget.group(1))
            doc.metadata ["price"] = price
        else:
            doc.metadata ["price"] = 0

    return Chroma.from_documents(embedding=embeddings, documents=split_docs)

vectorstore = setup_vectorstore()

@tool
def get_project_info(question):
    """
    Searches the internal project database. 
    Use this to find budget details, project descriptions, and metadata.
    """
    doc=vectorstore.similarity_search(question, k=3)
    return "\n\n".join ([f"INFO: {d.page_content} | METADATA: {d.metadata}" for d in doc])

@tool
def calculate_tax(amount):
    """"
    Calculate tax only ONCE. If you have the result, present it to the user and END.
    """
    final_price = amount * 1.21
    return f"The total budget including 21% VAT is ${final_price:.2f} USD."

class State(TypedDict):
    messages: Annotated[list, add_messages]

tools = [get_project_info, calculate_tax]
tool_node = ToolNode(tools)
llm = ChatGroq (model_name = "llama-3.1-8b-instant", temperature = 0).bind_tools(tools)

def call_model(state: State):
    trimmed_messages = state["messages"][-15:]
    messages_to_send = [system_message] + trimmed_messages
    response = llm.invoke(messages_to_send)
    return {"messages": [response]}

def should_continue(state: State):
    last_message = state["messages"][-1]
    if not last_message.tool_calls:
        return END
    return "tools"

workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge ("tools", "agent")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "final_fix_v1"}}

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["end", "exit"]:
        break

    for chunk in app.stream({"messages": [("user", user_input)]}, config):
        for node, values in chunk.items():
            content = values["messages"][-1].content
            if content:
                print(f"AI: ({node}): {content}")