class IceCream:
    # Defining the ice cream flavors and their prices
    _flavor_price = {
        "mint chocolate chip": 4.00,
        "chocolate": 3.00,
        "vanilla bean": 3.00,
        "banana": 3.50,
        "butter pecan": 3.50,
        "s'more": 4.00
    }

    # Defining the mix-ins and toppings
    _topping_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "storios": 1.00,
        "dig dogs": 1.00,
        "t&t's": 1.00,
        "cookie dough": 1.00,
        "pecans": 0.50
    }
    
    def __init__(self, flavor):
        if flavor.lower() not in self._flavor_price:
            raise ValueError(f"Invalid ice cream flavor.")
        self._flavor = flavor.lower()
        self._toppings = set()
        self._base_price = self._flavor_price[self._flavor]
    
    # Accessor for the base price
    def get_base_price(self):
        return self._base_price
    
    # Accessor for the ice cream flavor
    def get_flavor(self):
        return self._flavor
    
    # Add a topping, raise error if invalid
    def add_topping(self, topping):
        if topping.lower() not in self._topping_prices:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())
    
    # Count num of toppings
    def get_num_toppings(self):
        return len(self._toppings)
    
    # Get the total price of the ice cream
    def get_total(self):
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)
        return self._base_price + toppings_cost
