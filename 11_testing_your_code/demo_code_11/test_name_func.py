import unittest
from name_func import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Tests for name_function.py'''

    def test_first_last_name(self):
        '''Do names like 'Jane Jacobs' work?'''
        formatted_name = get_formatted_name('jane', 'jacobs')
        self.assertEqual(formatted_name, 'Jane Jacobs')

    def test_first_last_middle_name(self):
        '''Do names like 'John Fitzgerald Kennedy' work?'''
        formatted_name = get_formatted_name('john', 'kennedy', 'fitzgerald')
        self.assertEqual(formatted_name, 'John Fitzgerald Kennedy')

unittest.main()