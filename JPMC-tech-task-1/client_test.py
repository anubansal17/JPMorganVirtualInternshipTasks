import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quote0 = "ABC", 120.48, 121.2, (120.48 + 121.2) / 2

    self.assertEqual(getDataPoint(quotes[0]), quote0)
    for qt in quotes:
      self.assertEqual(getDataPoint(qt),(qt['stock'], qt['top_bid']['price'], qt['top_ask']['price'], (qt['top_bid']['price'] + qt['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
        {
            "top_ask": {
                "price": 119.2,
                "size": 36
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 120.48,
                "size": 109
            },
            "id": "0.109974697771",
            "stock": "ABC",
        },
        {
            "top_ask": {
                "price": 121.68,
                "size": 4
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 117.87,
                "size": 81
            },
            "id": "0.109974697771",
            "stock": "DEF",
        },
    ]
    """ ------------ Add the assertion below ------------ """
    for qt in quotes:
      Result = (
          qt["stock"],
          qt["top_bid"]["price"],
          qt["top_ask"]["price"],
          ((qt["top_bid"]["price"] + qt["top_ask"]["price"]) / 2),
      )
      self.assertEqual(getDataPoint(qt),Result)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatioAsSecondPriceZero(self):
    self.assertEqual(getRatio(100, 0), False)

  def test_getRatio_caclulateRatioAsFirstPriceZero(self):
    self.assertEqual(getRatio(0, 1233.3), 0)

  def test_getRatio_calculateRatioAgainstLesserValue(self):
    self.assertGreater(getRatio(123.32, 53.23), 1)

  def test_getRatio_calculateRatioAgainstGreaterValue(self):
    self.assertLess(getRatio(123.32, 153.23), 1)

  

if __name__ == '__main__':
    unittest.main()
