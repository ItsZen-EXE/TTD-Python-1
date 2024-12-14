class Drink:
    # list of bases
    _valid_bases = {"water", "sbrite", "pokecola", "Mr.Salt", "hill fog", "leaf wine"}
    # list of flavors
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    # list of sizes and their cost
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    
    # Initialize code
    def __init__(self, size):
        self._base = None
        self._flavors = set() # Set helps avoid duplicates
        self._size = None
        self._cost = 0.0
        self.set_size(size) # Initialize the cost based on the size
    
    # Create the base of the drinks
    def get_base(self):
        return self._base
    
    # Get the list of flavors added to the drink
    def get_flavors(self):
        return list(self._flavors)
    
    # Get the number of flavors to track how many were added.
    def get_num_flavors(self):
        return len(self._flavors)
    
    # Get the total cost
    def get_total(self):
        return self._cost
    
    # Make sure the base is valid using this code
    def set_base(self, base):
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"pick a proper base from {self._valid_bases}.")
    
    # Ensure the flavors being added are not duplicates
    def add_flavor(self, flavor):
        if flavor in self._valid_flavors:
            if flavor not in self._flavors: # Ensures that the flavors arent counted twice!
                self._cost += 0.15
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Do not pick duplicate flavors from {self._valid_flavors}.")
    
    # Reset the flavors and set multiple at once
    def set_flavors(self, flavors):
        if all(flavor in self._valid_flavors for flavor in flavors):
            new_flavors = set(flavors) - self._flavors
            self._cost += 0.15 * len(new_flavors) # Calculates additional costs for flavors not already added into the drink
            self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in self._valid_flavors] # Ensure the flavors chosen are valid
            raise ValueError(f"Invalid flavors: {invalid_flavors}. Choose a different flavor from {self._valid_flavors}.") 

    # # Ensure the flavors being picked are actually valid flavors    
    # def set_flavors(self, flavors):
    #     for flavor in flavors:
    #         if flavor not in self._valid_flavors:
    #             raise ValueError(f"pick proper flavors from {self._valid_flavors}.")
    #     self._flavors = set(flavors)
        
    # Make sure the size is valid using this code  
    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self._size = size
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size}. Choose a different size from {list(self._size_cost.keys())}.")

    