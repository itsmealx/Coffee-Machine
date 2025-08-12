from resource import MENU, resources

profit = 0
#TODO 3: Print report.
def print_report():
   print(f"Water: {resources["water"]}ml")
   print(f"Milk: {resources["milk"]}ml")
   print(f"Coffee: {resources["coffee"]}ml")
   print(f"Profit: ${profit}")


#Bonus functionality. I thought of suggesting other coffee based on the available resource
#and if the user really wants to have some coffee.
def suggest_alternatives() -> list[str]:
    """Return a list of alternatives based on the available resources."""
    alternatives = []
    #loop through the items in MENU and assigned the 'ingredients key' in ingredients
    for coffee, ing in MENU.items():
        ingredients = ing["ingredients"]
        can_make = True
        #loop through all the ingredients and compare if resource is enough to make the coffee
        for item, amount in ingredients.items():
            if resources.get(item) < amount:
                can_make = False
                break

        if can_make:
            alternatives.append(coffee)
    return alternatives


#TODO 4:  Check resources sufficient?
def is_resource_enough(ingredients: dict) -> bool:
    """Checks if there are enough resources to proceed."""
    #loop through item in ingredients and compare if there are enough resource to make a coffee
    for item in ingredients:
        if resources.get(item, 0) < ingredients[item]:
            print(f"Sorry there is not enough {item} for your selected coffee.")
            available = suggest_alternatives()
            if available:
                print("Available coffee: ", ", ".join(available))
            else:
                print("No available coffee for now.")
            return False
    return True


#TODO 5:  Process coins.
def process_payment() -> float:
    """Process payment and returns the accumulated total."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .10
    total += int(input("How many nickels? ")) * .05
    total += int(input("How many pennies? ")) * .01

    return total


#TODO 6: Check transaction successful?
def is_successful(payment: float, cost: float) -> bool:
    """Checks if payment is enough and returns True/False."""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print(f"Coffee price: ${cost}")
        print("Sorry that's not enough money. Money refunded.")
        return False


#TODO 7: Make Coffee.
def make_coffee(order_name: str, ingredients: dict):
    """Returns the name of the order and deducts ingredients used in resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order_name}. Enjoy! 🍵")



is_machine_on = True

while is_machine_on:
    menu_list = list(MENU.keys()) #dynamic list of menu
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    drink_name = input(f"What would you like? {menu_list}: ").lower()
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if drink_name == "off".lower():
        is_machine_on = False
    elif drink_name == "report".lower():
        print_report()
    elif drink_name in MENU:
        order = MENU[drink_name]
        if is_resource_enough(ingredients=order["ingredients"]):
            pay = process_payment()
            if is_successful(payment=pay, cost=order["cost"]):
                make_coffee(order_name=drink_name, ingredients=order["ingredients"])
    else:
        print("Please enter a valid coffee name.")
