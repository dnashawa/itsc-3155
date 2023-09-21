class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coin_values = {"dollar": 1.0, "half dollar": 0.5, "quarter": 0.25, "nickel": 0.05}
        totalVal = 0.0
        totalVal += int(input(f"How many whole dollars will you be inserting?\n")) * coin_values.get("dollar")
        print(f"Monetary Value Inserted: {totalVal}")
        totalVal += int(input(f"How many half-dollars will you be inserting?\n")) * coin_values.get("half dollar")
        print(f"Monetary Value Inserted: {totalVal}")
        totalVal += int(input(f"How many quarters will you be inserting?\n")) * coin_values.get("quarter")
        print(f"Monetary Value Inserted: {totalVal}")
        totalVal += int(input(f"How many nickels will you be inserting?\n")) * coin_values.get("nickel")
        print(f"Monetary Value Inserted: {totalVal}")
        return totalVal

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= int(cost):
            change = coins - cost
            if change > 0:
                print(f"Your change: ${change: .2f}")
            print("Payment success, sandwich being created.")
            return True
        else:
            print("Not enough money")
            return False
