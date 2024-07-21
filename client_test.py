import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Expected results
    expected_results = [
      ('ABC', 120.48, 121.2, 120.84),  # Average price (120.48 + 121.2) / 2
      ('DEF', 117.87, 121.68, 119.775)  # Average price (117.87 + 121.68) / 2
    ]

    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Expected results
    expected_results = [
      ('ABC', 120.48, 119.2, 119.84),  # Average price (120.48 + 119.2) / 2
      ('DEF', 117.87, 121.68, 119.775)  # Average price (117.87 + 121.68) / 2
    ]

    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)


  """ ------------ Add more unit tests ------------ """
  def test_getRation(self):
    price_a = 120.84
    price_b = 119.98
    self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

  def test_getRatio_priceBZero(self):
    price_a = 120.84
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 119.98
    self.assertEqual(getRatio(price_a, price_b), 0)



if __name__ == '__main__':
    unittest.main()
