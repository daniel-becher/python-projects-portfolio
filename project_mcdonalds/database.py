class FoodItem:
    def __init__(self, name, kcal, protein, carbs, fat):
        self.name = name
        self.kcal = kcal
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

DATABASE = {
    "Burgers": {
        "Hamburger": FoodItem("Hamburger", 258, 13, 29, 9),
        "Cheeseburger": FoodItem("Cheeseburger", 306, 16, 30, 13),
        "Double Cheeseburger": FoodItem("Double Cheeseburger", 457, 27, 31, 24),
        "Tasty Cheese": FoodItem("Tasty Cheese", 329, 16, 25, 18),
        "Big Mac": FoodItem("Big Mac", 510, 24, 40, 27),
        "McRoyal": FoodItem("McRoyal", 501, 29, 35, 27),
        "Double McRoyal": FoodItem("Double McRoyal", 798, 54, 38, 47),
        "Single Big Tasy Bacon": FoodItem("Single Big Tasy Bacon", 790, 35, 49, 50),
        "Double Big Tasy Bacon": FoodItem("Double Big Tasy Bacon", 1106, 57, 59, 71),

        "ChickenBurger": FoodItem("ChickenBurger", 342, 12, 49, 11),
        "Snack Wrap": FoodItem("Snack Wrap", 236, 10, 28, 9),
        "McChicken": FoodItem("McChicken", 427, 20, 45, 17),
        "Chicken McNuggets (4ks)": FoodItem("Chicken McNuggets (4ks)", 175, 11, 14, 8),
        "Chicken McNuggets (6ks)": FoodItem("Chicken McNuggets (6ks)", 262, 16, 21, 12),
        "Chicken McNuggets (9ks)": FoodItem("Chicken McNuggets (9ks)", 393, 25, 31, 19),
        "Chicken McNuggets (20ks)": FoodItem("Chicken McNuggets (20ks)", 873, 55, 68, 42),
        "Chicken Strips (2ks)": FoodItem("Chicken Strips (2ks)", 217, 14, 19, 10),
        "Chicken Strips (4ks)": FoodItem("Chicken Strips (4ks)", 433, 28, 37, 19),
        "Filet-O-Fish": FoodItem("Filet-O-Fish", 327, 13, 36, 13),
        },

    "Sides": {
        "Fries (S)": FoodItem("Fries (S)", 229, 3, 29, 11),
        "Fries (M)": FoodItem("Fries (M)", 327, 4, 41, 15),
        "Fries (L)": FoodItem("Fries (L)", 430, 5, 54, 20),
        "Salad": FoodItem("Salad", 55, 1, 10, 0)

    },
    "Sauces": {
        "Sweet and Sour": FoodItem("Sweet and sour", 42, 0, 9, 0),
        "Ketchup": FoodItem("Ketchup", 14, 0, 3, 0),
        "Mayo": FoodItem("Mayo", 20, 0, 1, 1),
        "Hellmann's": FoodItem("Hellmann's", 120, 0, 0, 12),
        "BBQ": FoodItem("BBQ", 47, 0, 10, 0),
        "Curry": FoodItem("Curry", 39, 0, 8, 1),
        "Mustard": FoodItem("Mustard", 54, 0, 6, 3),
        "Lemon Chilli": FoodItem("Lemon Chilli", 59, 0, 14, 1),
        "Caesar dressing": FoodItem("Caesar dressing", 103, 1, 3, 9),
        "1000 Islands dressing": FoodItem("1000 Islands dressing", 104, 0, 3, 10),
        "Yogurt dressing": FoodItem("Yogurt dressing", 105, 0, 3, 9),
        "Cheese dressing": FoodItem("Cheese dressing", 126, 1, 2, 12),
        "Olive oil and Balsamic vinegar": FoodItem("Olive oil and Balsamic vinegar", 81, 0, 1, 8),
        "None": FoodItem("None", 0, 0, 0, 0)
    },

    "Drinks": {
        "Coca-Cola": FoodItem("Coca-Cola", 208, 0, 52, 0),
        "Coca-Cola Zero": FoodItem("Coca-Cola Zero", 0, 0, 0, 0),
        "Fanta": FoodItem("Fanta", 192, 0, 48, 0),
        "Sprite": FoodItem("Sprite", 136, 0, 33, 0),
        "IceTea": FoodItem("IceTea", 90, 2, 22, 2),
        "Apple juice": FoodItem("Apple juice", 106, 0, 27, 0), 
        "Orange juice": FoodItem("Orange juice", 94, 1, 22, 0),
        "Water": FoodItem("Water", 0, 0, 0, 0),
        "Tea": FoodItem("Tea", 0, 0, 0, 0),
        "Ice cream Coffee": FoodItem("Ice cream Coffee", 151, 3, 25, 4),
        "Coffee Latte": FoodItem("Coffee Latte", 75, 5, 7, 3),
        "Cappuccino": FoodItem("Cappuccino", 54, 4, 5, 2),
        "Americano": FoodItem("Americano", 0, 0, 0, 0),
        "Americano with milk": FoodItem("Americano with milk", 32, 1, 2, 1),
        "Espresso/Espresso Grande/Double Espresso": FoodItem("Espresso/Espresso Grande/Double Espresso", 0, 0, 0, 0),
        "Toasted Marshmallow Cappuccino": FoodItem("Toasted Marshmallow Cappuccino", 113, 3, 23, 3)
    }

}

# Sjednotí všechny pod-slovníky do jednoho velkého
FLAT_DATABASE = {}
for cat in DATABASE:
    FLAT_DATABASE.update(DATABASE[cat])
