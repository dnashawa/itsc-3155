### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < quantity:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(self.machine_resources):
            for ingredient, quantity in order_ingredients.items():
                self.machine_resources[ingredient] -= quantity
            print(f"Successfully made sandwich")
        else:
            print(f"Insufficient resources to create sandwich")

# Make an instance of SandwichMachine class and write the rest of the codes #


sm = SandwichMachine(resources)
print("\nWelcome to Dylan Nashawaty's sandwich shop!")
resVal = input("What would you like? (small/medium/large/off/report)\n")
balanceDue = sm.machine_resources


if resVal.lower().strip() == "small":
    sm.make_sandwich("small", sm.machine_resources)
    balanceDue = 5.50

elif resVal.lower().strip() == "medium":
    sm.make_sandwich("medium", sm.machine_resources)
    balanceDue = 6.50

elif resVal.lower().strip() == "large":
    sm.make_sandwich("large", sm.machine_resources)
    balanceDue = 7.50

elif resVal.lower().strip() == "off":
    print("Exiting System...")
    exit(0)

elif resVal.lower().strip() == "report":
    print(sm.machine_resources)
    input("Press a key to close report")
    exit(0)

else:
    print("Error taking input")
    exit(0)

paymentVal = 0.00

moneyType = input("How will you be paying? (large dollar/half dollar/quarter/nickel)\n")
loopNum = 0

while paymentVal < balanceDue:
     
    if loopNum != 0:
        print(f"Current balance: ${paymentVal} \nTotal Cost: ${balanceDue}")
        moneyType = input("Balance not met, what else will you insert? (large dollar/half dollar/quarter/nickel)")

    if moneyType == "large dollar":
        paymentVal += 1.00
    elif moneyType == "half dollar":
        paymentVal += 0.50
    elif moneyType == "quarter":
        paymentVal += 0.25
    elif moneyType == "nickel":
        paymentVal += 0.05
    else:
        print("Invalid monetary type!")
    loopNum += 1
