class Food:
    # Defining the food
    _food_price = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90
    }
    #Defining the toppings
    _topping_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }
    
    def __init__(self, food_type):
        if food_type.lower() not in self._food_price:
            raise ValueError(f"Invalid food type.")
        self._type = food_type.lower()
        self._toppings = set()
        self._base_price = self._food_price[self._type]
    
    # Accessor for the base price
    def get_base_price(self):
        return self._base_price
    
    # Accessor for the food type
    def get_type(self):
        return self._type
    
    # Add a topping, raise error if invalid
    def add_topping(self, topping):
        if topping.lower() not in self._topping_prices:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())
    
    #Count num of toppings
    def get_num_toppings(self):
        return len(self._toppings)
    
    # Get the total price of the food
    def get_total(self):
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)
        return self._base_price + toppings_cost
    
    