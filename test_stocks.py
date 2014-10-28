import unittest
from stocks import Stocks

__author__ = "hbansal"
__version__ = "0.1.1"


class StocksTestSuite(unittest.TestCase):

    def setUp(self):
        """pre-test"""
        pass

    def tearDown(self):
        """post-test"""
        pass

    def test_csv_file_not_exist(self):
        invalid_fname = "test.csv"
        self.assertRaises(Exception, Stocks, invalid_fname)

    def test_csv_file_exist(self):
        valid_fname = r"test_shares_data.csv"
        Stocks(valid_fname)

    def test_correct_headers_and_sort_data(self):
        valid_fname = "test_parse_data.csv"
        exp_headers = ['Year', 'Month', 'Company-A', 'Company-B', 'Company-C']
        exp_data = {'Company-A': [],
                    'Company-B': [('1990', 'Apr')],
                    'Company-C': [('1990', 'Jan'),
                                  ('1990', 'Feb'),
                                  ('1990', 'Mar')]}
        obj_stocks = Stocks(valid_fname)
        parsed_data = obj_stocks.parse_data(valid_fname)
        self.assertEqual(parsed_data[0], exp_headers)
        self.assertEqual(parsed_data[1], exp_data)

    def test_wrong_header_data(self):
        valid_fname = "test_parse_data.csv"
        exp_headers = ['Year', 'Month', 'Company-D', 'Company-B', 'Company-C']
        obj_stocks = Stocks(valid_fname)
        parsed_data = obj_stocks.parse_data(valid_fname)
        self.assertNotEqual(parsed_data[0], exp_headers)

    def test_wrong_sort_data(self):
        valid_fname = "test_parse_data.csv"
        exp_data = {'Company-A': [('1990', 'Jan')],
                    'Company-B': [('1990', 'Apr')],
                    'Company-C': [('1990', 'Feb'),
                                  ('1990', 'Mar')]}
        obj_stocks = Stocks(valid_fname)
        parsed_data = obj_stocks.parse_data(valid_fname)
        self.assertNotEqual(parsed_data[1], exp_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)
