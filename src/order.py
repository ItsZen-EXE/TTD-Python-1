from drink import Drink
from food import Food
from ice_cream import IceCream

class Order:
    _tax_rate = 0.0725  # Declare the tax rate globally

    def __init__(self):
        self._items = []

    # Get the list of items added to the order (drinks, food, or ice creams)
    def get_items(self):
        return self._items

    # Get the total number of items added to the order
    def get_num_items(self):
        return len(self._items)

    # Return the sum of all items (drinks, food, and ice creams) added together that have been ordered
    def get_total(self):
        return sum(item.get_total() for item in self._items)

    # Return the sum of the order with the tax rate
    def get_tax(self):
        return self.get_total() * (1 + self._tax_rate)

    # Generate the receipt for the full order
    def get_receipt(self):
        receipt_data = {
            "number_items": self.get_num_items(),
            "items": [],
            "subtotal": self.get_total(),
            "tax": self.get_total() * self._tax_rate,
            "grand_total": self.get_tax()
        }

        for i, item in enumerate(self._items):
            if isinstance(item, Drink):
                item_data = {
                    "number": i + 1,
                    "type": "Drink",
                    "base": item.get_base(),
                    "size": item.get_size(),
                    "flavors": ", ".join(item.get_flavors()),
                    "total_cost": item.get_total(),
                }
            elif isinstance(item, Food):
                item_data = {
                    "number": i + 1,
                    "type": "Food",
                    "food_type": item.get_type(),
                    "total_cost": item.get_total(),
                }
            elif isinstance(item, IceCream):
                item_data = {
                    "number": i + 1,
                    "type": "Ice Cream",
                    "flavor": item.get_flavor(),
                    "toppings": ", ".join(item._toppings),
                    "total_cost": item.get_total(),
                }
            receipt_data["items"].append(item_data)

        return receipt_data

    # Used to add items to the order (drinks, food, or ice cream)
    def add_item(self, item):
        if isinstance(item, (Drink, Food, IceCream)):
            self._items.append(item)
        else:
            raise ValueError(f"Only drinks, food, or ice creams can be added to this order.")

    # Used to remove items from the order
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise ValueError(f"Invalid, cannot remove")
