import unittest
from nytapiclient.bestsellers import BestSellers


class BestSellersTest(unittest.TestCase):

    def test_best_sellers_get_list(self):
        b = BestSellers()
        list = b.get_list('combined-print-and-e-book-fiction')
        import pprint
        pprint.pprint(list[0])
        self.assertTrue(len(list) > 0)

    def test_best_sellers_get_list_names(self):
        b = BestSellers()
        list_names = b.get_list_names()
        self.assertTrue(len(list_names) > 0)