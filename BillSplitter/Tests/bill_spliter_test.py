import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bill_splitter

class BillSpliterTest(unittest.TestCase):
    def test_A(self):
        self.assertEqual('meow', bill_splitter.meow())

    def test_check_number(self):
        self.assertFalse(bill_splitter.check_number('meow'))
        self.assertTrue(bill_splitter.check_number('1'))
        self.assertTrue(bill_splitter.check_number(1))

    def test_check_greater_than_zero(self):
        self.assertFalse(bill_splitter.check_greater_than_zero(0))
        self.assertFalse(bill_splitter.check_greater_than_zero(-1))
        self.assertTrue(bill_splitter.check_greater_than_zero(5))

if __name__ == '__main__':
    unittest.main()
