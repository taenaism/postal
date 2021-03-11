import unittest
from main import main
from postcode import ApiError


class TestCase(unittest.TestCase):

    def test_success(self):
        self.assertTrue(main('CB3 0FA'), True)

    def test_no_input(self):
        self.assertEqual(main(), 'no input')

    def test_invalid(self):
        self.assertEqual(main('XXX'), 'invalid')

    def test_no_query(self):
        with self.assertRaises(ApiError):
            main('?')


if __name__ == "__main__":
    unittest.main(buffer=True, verbosity=2)
# py -m unittest postal.test -bv
