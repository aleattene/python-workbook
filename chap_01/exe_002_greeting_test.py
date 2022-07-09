""" To start the tests, type from CLI: pytest """

import unittest
from exe_002_greeting import print_greetings


class Exe002(unittest.TestCase):

    def print_greetings(self):
        self.assertEqual(print_greetings(), 'Hello Alessandro Attene.')


if __name__ == '__main__':
    """ The following instruction executes the tests
     by discovering all classes present in this file
     that inherit from unittest.TestCase.
     """
    unittest.main()
