class Drink:
    # list of bases
    _valid_bases = {"water", "sbrite", "pokecola", "Mr.Salt", "hill fog", "leaf wine"}
    # list of flavors
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    
    # Initialize code
    def __init__(self):
        self._base = None
        self._flavors = set() # Set helps avoid duplicates
    
    # Create the base of the drinks
    def get_base(self):
        return self._base
    
    # Get the list of flavors added to the drink
    def get_flavors(self):
        return list(self._flavors)
    
    # Get the number of flavors to track how many were added.
    def get_num_flavors(self):
        return len(self._flavors)
    
    # Make sure the base is valid using this code
    def set_base(self, base):
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"pick a proper base from {self._valid_bases}.")
    
    # Ensure the flavors being added are not duplicates
    def add_flavor(self, flavor):
        if flavor in self._valid_flavors:
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Do not pick duplicate flavors from {self._valid_flavors}.")
    
    # Ensure the flavors being picked are actually valud flavors    
    def set_flavors(self, flavors):
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"pick proper flavors from {self._valid_flavors}.")
        self._flavors = set(flavors)
    
        
class Order:
    # Create an array for the starting point of the order
    def __init__(self):
        self._items = []
    
    # Get the list of drinks added to the order   
    def get_items(self):
        return self._items
    
    # Grab the total number of items added to the order
    def get_total(self):
        return len(self._items)
    
    # Generate the receipt for the full order
    def get_receipt(self):
        receipt = "Your order receipt:\n"
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            flavors = ", ".join(drink.get_flavors())
            receipt += f"{i + 1}: base - {base}, Flavors - {flavors}\n"
        return receipt
    
    # Used to add items to the order
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError(f"You can only add drinks to this order.")
    
    # Used to remove items to the order    
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise ValueError(f"Invalid, cannot remove")