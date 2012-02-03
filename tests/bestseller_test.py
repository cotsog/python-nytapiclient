import unittest

from nytapiclient.bestseller import BestSeller

class BestSellerTest(unittest.TestCase):
    
    def test_bestseller_constructor(self):
        b = BestSeller()
        self.assertTrue(len(b.getListNames()) > 0, 'List is empty!')
