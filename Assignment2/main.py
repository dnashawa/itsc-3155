import data
import sandwich_maker
import cashier
# Three modules (data, sandwich_maker, cashier) should be imported at the top of main.py. #
resources = data.resources # Create two variables based on data dictionaries (resources and recipes)
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier


def main():
    print(f"Welcome to Dylan's Sandwich Shop")
    buyAnother = True
    smallCost = recipes["small"]["cost"]
    medCost = recipes["medium"]["cost"]
    lgCost = recipes["large"]["cost"]

    while buyAnother:
        sizeVal = input("What do you want to do?\nSelect sandwich size or enter other command. (small/medium/large/report/off)\n")
        match sizeVal:
            case "small":
                print(f"Your cost will be {smallCost}")
                cashier_instance.transaction_result(cashier_instance,cashier_instance.process_coins(cashier_instance),recipes["small"]["cost"])
                sandwich_maker_instance.make_sandwich("small", sandwich_maker_instance.machine_resources)
            case "medium":
                print(f"Your cost will be {medCost}")
                cashier_instance.transaction_result(cashier_instance, cashier_instance.process_coins(cashier_instance), recipes["medium"]["cost"])
                sandwich_maker_instance.make_sandwich("medium", sandwich_maker_instance.machine_resources)
            case "large":
                print(f"Your cost will be {lgCost}")
                cashier_instance.transaction_result(cashier_instance, cashier_instance.process_coins(cashier_instance), recipes["large"]["cost"])
                sandwich_maker_instance.make_sandwich("large", sandwich_maker_instance.machine_resources)
            case "off":
                print("Exiting system...")
                exit(0)
            case "report":
                print(f"Printing report...")
                breadSlices = sandwich_maker_instance.machine_resources["bread"]
                print(f"Bread Slices Remaining: {breadSlices}")
                hamSlices = sandwich_maker_instance.machine_resources["ham"]
                print(f"Ham Slices Remaining: {hamSlices}")
                cheeseOz = sandwich_maker_instance.machine_resources["cheese"]
                print(f"Cheese Ounces Remaining: {cheeseOz}")
            case _:
                print(f"Invalid Entry")
        if input("Do you want to issue another command? Y/N\n") == "n":
            buyAnother = False
            exit(0)


if __name__ == "__main__":
    main()
