import tkinter as tk
import requests

# Fetching live exchange rates from the Czech National Bank
url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

response = requests.get(url)

if response.status_code == 200:
    data = response.text
else:
    print("Error during data downloading.")



lines = data.split("\n")

found = False

for line in lines:
    parts = line.split("|")
    if "EUR" in line and len(parts) > 4:
        rate =  float(parts[4].replace(",", "."))
        found = True
        
if not found:
    print ("Currency not found.")


def calc():
    amount = entry.get()
    
    try:
        result = round(float(amount) / rate, 2)
        label.config(text=f"Result: {result} EUR", fg="green")
        entry.delete(0, tk.END)
    except ValueError:
        label.config(text="Please enter a number!", fg="red")
    

root = tk.Tk()
root.title("Currency converter")
root.geometry("300x200")

tk.Label(root, text="How much CZK do you want to convert?").pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Convert", command=calc)
button.pack()

label = tk.Label(root, text="Nothing yet...", font=("Verdana", 12))
label.pack(pady=10)

root.mainloop()
