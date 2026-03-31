import data

MENU = data.MENU
VALID_DRINKS = MENU.keys()


class CoffeeMachine:


    def __init__(self):
        self.is_working = True
        self.profit = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }


    def turn_off(self):
        self.is_working = False


    def print_report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")
        print(f"Money: ${self.profit:.2f}")


    def ask_user_request(self):
        drinks = "/".join(VALID_DRINKS)
        return input(f"What would you like? ({drinks}): ")


    def is_resource_sufficient(self, order_ingredients):
        """Returns True if there are enough resources available, False if resources insufficient."""
        for item in order_ingredients:
            if order_ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True


    def get_int_input(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Using 0.")
            return 0


    def process_coins(self):
        """Returns total money received."""
        coins = {
            "quarters": 0.25,
            "dimes": 0.1,
            "nickles": 0.05,
            "pennies": 0.01,
        }
        print("Please insert coins.")

        total = 0
        for coin, value in coins.items():
            total += self.get_int_input(f"How many {coin}: ") * value
        return total


    def is_transaction_successful(self, money_received, drink_cost):
        """Returns True if money_received is >= drink cost, False otherwise."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            self.profit += drink_cost
            return True
        else:
            print("Sorry, that`s not enough money. Money refunded.")
            return False


    def make_coffee(self, drink_name, order_ingredients):
        """Deducts ingredients and cost of the drink from machine resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")


    def make_order(self, drink_name):
        drink = MENU[drink_name]

        if not self.is_resource_sufficient(drink["ingredients"]):
            return

        payment = self.process_coins()

        if not self.is_transaction_successful(payment, drink["cost"]):
            return

        self.make_coffee(drink_name, drink["ingredients"])


    def handle_choice(self, user_choice):
        if user_choice == "off":
            self.turn_off()

        elif user_choice == "report":
            self.print_report()

        elif user_choice in MENU:
            self.make_order(user_choice)

        else:
            print("Invalid choice. Please try again.")


machine = CoffeeMachine()

while machine.is_working:
    choice = machine.ask_user_request()
    machine.handle_choice(choice)



