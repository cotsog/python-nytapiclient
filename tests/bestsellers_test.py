import unittest
from nytapiclient.bestsellers import BestSellers


class BestSellersTest(unittest.TestCase):

    def test_best_sellers_get_list_names(self):
        b = BestSellers()
        list_names = b.get_list_names()
        import pprint
        pprint.pprint(list_names)
        self.assertTrue(len(list_names) > 0)
