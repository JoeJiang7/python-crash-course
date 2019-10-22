import unittest

class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raises = 500):
        self.salary += raises


class TestSalary(unittest.TestCase):
    salary = 500
    def setUp(self):
        self.people1 = Employee('joey', 'dan', 500 )

    def test_give_default_raise(self):
        self.people1.give_raise()
        self.assertEqual(1000, self.people1.salary)

    def test_give_custom_raise(self):
        self.people1.give_raise(1000)
        self.assertEqual(1500, self.people1.salary)


unittest.main()


