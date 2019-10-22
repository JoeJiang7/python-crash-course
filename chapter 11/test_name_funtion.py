from name_function import get_formatted_name
import unittest


class NameTestCase(unittest.TestCase):
    """测试name-function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('joe', 'jiang')
        self.assertEqual(formatted_name, 'Joe Jiang')
if __name__== '__main__':
    unittest.main()