""" To start the tests, type from CLI: pytest """

import unittest
from exe_001_print_address import print_address


class Exe001(unittest.TestCase):

    def test_print_address(self):
        name = 'ATTENE ALESSANDRO'
        address = 'Via della Speranza, 13'
        cap = '20019'
        city = 'Milano (MI)'
        complete_address = f"{name}\n{address}\n{cap} - {city}"
        self.assertEqual(print_address(complete_address), complete_address)


if __name__ == '__main__':
    """ The following instruction executes the tests
     by discovering all classes present in this file
     that inherit from unittest.TestCase.
     """
    unittest.main()
