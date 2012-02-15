import unittest
from nytapiclient.bestsellers import BestSellers


class BestSellersTest(unittest.TestCase):

    __API_KEY = '9b10adbc72536a67930154a2bbcfedba:4:62210421'

    def test_best_sellers_get_book_list(self):
        b = BestSellers(self.__API_KEY)
        book_list = b.get_list('combined-print-and-e-book-fiction')
        import pprint
        pprint.pprint(book_list)
        self.assertTrue(len(book_list) > 0)

    def test_best_sellers_get_book_list_names(self):
        b = BestSellers(self.__API_KEY)
        list_names = b.get_list_names()
        import pprint
        pprint.pprint(list_names)
        self.assertTrue(len(list_names) > 0)
