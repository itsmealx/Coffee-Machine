MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def suggest_alternatives():
    alternatives = []
    for coffee, details in MENU.items():
        ingredients = details["ingredients"]
        can_make = True

        for item, amount in ingredients.items():
            if resources.get(item) < amount:
                can_make = False
                break

        if can_make:
            alternatives.append(coffee)
    return alternatives



alt = []
# for coffee, details in MENU.items():
#     ingredients = details["ingredients"]
#     if all(resources.get(item, 0) > amount for item, amount in ingredients.items()):
#         alt.append(coffee)


# for coffee, details in MENU.items():
#     ingredients = details["ingredients"]
#     can_make = True
#
#     for item, amount in ingredients.items():
#         if resources.get(item) < amount:
#             can_make = False
#             break
#     if can_make:
#         alt.append(coffee)



