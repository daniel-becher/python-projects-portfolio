import requests
import tkinter as tk

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

response = requests.get(url)

if response.status_code == 200:
    data = response.text
else:
    print("Error during downloading data.")

lines = data.split("\n")

def get_exchange_rate():
    target_currency = currency_entry.get().upper()

    for line in lines:
        data_columns = line.split("|")
        
        if len(data_columns) > 4 and target_currency == data_columns[3]:
            amount = float(data_columns[2])
            exchange_rate = float(data_columns[4].replace(",", "."))
            final_rate = exchange_rate / amount
            return final_rate, target_currency
            
    return None, None
        

def conversion():
    input_value = amount_entry.get()
    exchange_rate, code = get_exchange_rate()

    if exchange_rate is None:
        result_label.config(text="Invalid currency code!", fg="red")
        return

    try:
        result = round(float(input_value) / exchange_rate, 2)
        result_label.config(text=f"Result: {input_value} CZK = {result} {code}.", fg="green")
        amount_entry.delete(0, tk.END)
    except ValueError:
        result_label.config(text="Enter a number.", fg="red")


root = tk.Tk()
root.title("Money converter")
root.geometry("300x250")

tk.Label(root, text="How much CZK do you want to convert?: ").pack(pady=10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=10)

label_2 = tk.Label(root, text="What currency do you want to exchange to?: ")
label_2.pack(pady=10)

currency_entry = tk.Entry(root)
currency_entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=conversion)
convert_button.pack()

result_label = tk.Label(root, text="Nothing yet...")
result_label.pack()


root.mainloop()
