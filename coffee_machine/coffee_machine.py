from source_data import MENU
from source_data import resources

lets_continue = True
rest_of_ingredients = resources

def report(data):
    print(f"Voda: {data['water']}ml")
    print(f"Mléko: {data['milk']}ml")
    print(f"Káva: {data['coffee']}g")

def coins():
    print("Prosím vložte mince (1, 2, 5, 10, 20, 50)")
    suma = int(input("1 Kč: "))
    suma += int(input("2 Kč: ")) * 2
    suma += int(input("5 Kč: ")) * 5
    suma += int(input("10 Kč: ")) * 10
    suma += int(input("20 Kč: ")) * 20
    suma += int(input("50 Kč: ")) * 50
    print(f"Celkem vloženo: {suma} Kč.")
    return suma

def is_resource_sufficient(drink_name):
    """Vrátí True, pokud je dost surovin, jinak False."""
    for item, amount in MENU[drink_name]["ingredients"].items():
        if amount > rest_of_ingredients.get(item, 0):
            print(f"Bohužel není dostatek ingredience: {item}.")
            return False
    return True

def make_coffee(drink_name):
    """Odečte suroviny z automatu."""
    for item, amount in MENU[drink_name]["ingredients"].items():
        rest_of_ingredients[item] -= amount
    print(f"Vaše {drink_name} ☕ je hotové. Dobrou chuť!")


while lets_continue:
    user_choice = input("\nCo byste si dal? (espresso/latte/cappuccino/off): ").lower()

    if user_choice == "off":
        lets_continue = False
    elif user_choice == "report":
        report(rest_of_ingredients)
    elif user_choice in MENU:
        drink = MENU[user_choice]
        
        if is_resource_sufficient(user_choice):
            print(f"Cena za {user_choice} je {drink['cost']} Kč.")
            payment = coins()
            
            if payment >= drink["cost"]:
                change = payment - drink["cost"]
                if change > 0:
                    print(f"Zde je drobák zpět: {change} Kč.")
                
                make_coffee(user_choice)
            else:
                print(f"Nedostatek peněz. Peníze {payment} Kč vráceny.")
    else:
        print("Neplatná volba, zkus to znovu.")