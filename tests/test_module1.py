import unittest
from src.Module1 import Drink, Order  # import the drink and order classes

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

