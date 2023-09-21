import data
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources[ingredient] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        match sandwich_size:
            case "small":
                if self.check_resources(data.recipes["small"]["ingredients"]):
                    for ingredients, quantity in order_ingredients.items():
                        self.machine_resources[ingredients] -= quantity
                    print(f"Successfully made sandwich")
                else:
                    print(f"Insufficient resources to make sandwich")
            case "medium":
                if self.check_resources(data.recipes["medium"]["ingredients"]):
                    for ingredients, quantity in order_ingredients.items():
                        self.machine_resources[ingredients] -= quantity
                    print(f"Successfully made sandwich")
                else:
                    print(f"Insufficient resources to make sandwich")
            case "large":
                if self.check_resources(data.recipes["large"]["ingredients"]):
                    for ingredients, quantity in order_ingredients.items():
                        self.machine_resources[ingredients] -= quantity
                    print(f"Successfully made sandwich")
                else:
                    print(f"Insufficient resources to make sandwich")