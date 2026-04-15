import tkinter as tk
from database import DATABASE, FLAT_DATABASE

current_mode = "menu"
cart_items = []
counts = {}

def show_single():
    global current_mode
    current_mode = "single"
    frame_menu.pack_forget()
    frame_single.pack(pady=20, before=calc_btn)

def show_menu():
    global current_mode
    current_mode = "menu"
    frame_single.pack_forget()
    frame_menu.pack(pady=20, before=calc_btn)

def add_to_cart():
    items_to_process = []
    
    if current_mode == "single":
        items_to_process.append(FLAT_DATABASE[single_var.get()])
    else:
        items_to_process.extend([
            DATABASE["Sauces"][sauce_var.get()],
            DATABASE["Drinks"][drink_var.get()],
            DATABASE["Sides"][side_var.get()],
            DATABASE["Burgers"][burger_var.get()]
        ])

    for item in items_to_process:
        cart_items.append(item)
        
        if item.name in counts:
            counts[item.name] += 1
        else:
            counts[item.name] = 1

    cart_listbox.delete(0, tk.END)
    for name, count in counts.items():
        cart_listbox.insert(0, f"{count}x {name}")

    calculate()

def clear_cart():
    cart_items.clear()
    counts.clear()
    cart_listbox.delete(0, tk.END)
    calculate()

def calculate():
    total_kcal = sum(item.kcal for item in cart_items)
    total_protein = sum(item.protein for item in cart_items)
    total_carbs = sum(item.carbs for item in cart_items)
    total_fat = sum(item.fat for item in cart_items)

    result_label.config(
        text=f"TOTAL:\nCalories: {total_kcal} kcal\n"
             f"Protein: {total_protein}g | Carbs: {total_carbs}g | Fat: {total_fat}g"
    )

root = tk.Tk()
root.title("McDonald's Nutri Calc")
root.geometry("600x600")

tk.Label(root, text="What did you eat?", font=("Arial", 12, "bold")).pack(pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Single product", command=show_single).pack(side="left", padx=5)
tk.Button(btn_frame, text="Menu", command=show_menu).pack(side="left", padx=5)

frame_single = tk.Frame(root)
tk.Label(frame_single, text="Choose a product:", font=("Arial", 12, "bold")).pack()

all_items = []
for cat in DATABASE:
    all_items.extend(DATABASE[cat].keys())

single_var = tk.StringVar(root)
single_var.set(all_items[0])
tk.OptionMenu(frame_single, single_var, *all_items).pack()

frame_menu = tk.Frame(root)
tk.Label(frame_menu, text="Build a menu:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=10)


burger_var = tk.StringVar(root)
side_var = tk.StringVar(root)
drink_var = tk.StringVar(root)
sauce_var = tk.StringVar(root)

burger_var.set(list(DATABASE["Burgers"].keys())[0])
side_var.set(list(DATABASE["Sides"].keys())[0])
drink_var.set(list(DATABASE["Drinks"].keys())[0])
sauce_var.set(list(DATABASE["Sauces"].keys())[0])

tk.Label(frame_menu, text="Main dish:").grid(row=1, column=0, padx=5)
tk.OptionMenu(frame_menu, burger_var, *DATABASE["Burgers"]).grid(row=2, column=0, padx=5)

tk.Label(frame_menu, text="Side:").grid(row=1, column=1, padx=5)
tk.OptionMenu(frame_menu, side_var, *DATABASE["Sides"]).grid(row=2, column=1, padx=5)

tk.Label(frame_menu, text="Drink:").grid(row=1, column=2, padx=5)
tk.OptionMenu(frame_menu, drink_var, *DATABASE["Drinks"]).grid(row=2, column=2, padx=5)

tk.Label(frame_menu, text="Sauce:").grid(row=1, column=3, padx=5)
tk.OptionMenu(frame_menu, sauce_var, *DATABASE["Sauces"]).grid(row=2, column=3, padx=5)


calc_btn = tk.Button(root, text="ADD TO CART", font=("Arial", 12, "bold"), bg="#FFBC0D", command=add_to_cart)
calc_btn.pack(pady=20)

result_label = tk.Label(root, text="Choose your food and click on 'ADD TO CART'", font=("Arial", 11))
result_label.pack(pady=10)

tk.Label(root, text="Your order:").pack()
cart_listbox = tk.Listbox(root, width=50, height=6)
cart_listbox.pack(pady=5)

tk.Button(root, text="Empty cart", command=clear_cart).pack()

show_menu()

root.mainloop()