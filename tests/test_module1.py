import unittest
# import the drink and order classes
from src.drink import Drink
from src.food import Food
from src.order import Order
class TestDrink(unittest.TestCase):

    def setUp(self): #setUp runs before each test!
        # Create a drink before each test with size 'medium'
        self.drink = Drink('medium')

    def test_get_base(self):
        # Test to make sure the base is none to start with
        self.assertIsNone(self.drink.get_base())

    def test_get_flavors(self):
        # Test that the initial flavors list is empty
        self.assertEqual(self.drink.get_flavors(), [])

    def test_get_num_flavors(self):
        # Test that the number of flavors is initially zero, since no flavors have been added
        self.assertEqual(self.drink.get_num_flavors(), 0)

    def test_get_total(self):
        # Test that the total cost is initially the base cost of a medium drink
        # When initialized, a medium drink costs $1.75
        self.assertEqual(self.drink.get_total(), 1.75)

    def test_set_base(self):
        # Set the drink base to 'water' and check if the base is correctly updated to be water
        self.drink.set_base('water')
        self.assertEqual(self.drink.get_base(), 'water')

    def test_set_invalid_base(self):
        # Test setting an invalid base (not in the valid base list). This should raise an error.
        with self.assertRaises(ValueError):
            self.drink.set_base('invalid_base')


class TestFood(unittest.TestCase):

    def setUp(self): #setUp runs before each test!
        # Create food before each test
        self.hotdog = Food("hotdog")
        self.ice_cream = Food("ice cream")
    
    # Test for get_base_price method to ensure it returns correctly
    def test_get_base_price(self):
        self.assertEqual(self.hotdog.get_base_price(), 2.30)
        self.assertEqual(self.ice_cream.get_base_price(), 3.00)

    # Test for get_type method to ensure it returns correctly
    def test_get_type(self):
        self.assertEqual(self.hotdog.get_type(), "hotdog")
        self.assertEqual(self.ice_cream.get_type(), "ice cream")

    # Test for add_topping method with valid topping
    def test_add_topping(self):
        self.ice_cream.add_topping("cherry")
        self.assertEqual(self.ice_cream.get_num_toppings(), 1)
    
    # Test for add_topping method with invalid topping
    def test_add_invalid_topping(self):
        with self.assertRaises(ValueError):
            self.hotdog.add_topping("invalid_topping")
    
    # Test for get_num_toppings method
    def test_get_num_toppings(self):
        self.ice_cream.add_topping("whipped cream")
        self.ice_cream.add_topping("caramel sauce")
        self.assertEqual(self.ice_cream.get_num_toppings(), 2)
    
    # Test for get_total_price method
    def test_get_total_price(self):
        self.hotdog.add_topping("chili")
        self.hotdog.add_topping("ketchup")
        self.assertEqual(self.hotdog.get_total_price(), 2.90)  # 2.30 + 0.60 + 0.00


class TestOrder(unittest.TestCase):

    def setUp(self): #setUp runs before each test!
        # Create a new order and a small drink before each test
        self.order = Order()
        self.drink = Drink('small')
        # Add the drink to the order for testing
        self.order.add_item(self.drink)

    def test_get_items(self):
        # Test that the order contains the one drink that was added
        self.assertEqual(self.order.get_items(), [self.drink])

    def test_get_num_items(self):
        # Test that the number of items in the order is 1, as only one drink was added
        self.assertEqual(self.order.get_num_items(), 1)

    def test_get_total(self):
        # Test that the total cost of the order is the cost of the one small drink
        # A small drink costs $1.50
        self.assertEqual(self.order.get_total(), 1.50)

    def test_get_tax(self):
        # Test that the total with tax is calculated correctly
        # it should be the cost of a small drink ($1.50) multiplied by (1 + the tax rate of 0.0725)
        expected_tax = 1.50 * 1.0725
        self.assertAlmostEqual(self.order.get_tax(), expected_tax, places=2) # places=2 specifies the number of decimal places there should be
        
if __name__ == '__main__':
    unittest.main()  # Runs the unit tests

