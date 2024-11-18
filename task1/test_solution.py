import unittest
from solution import sum_two


class TestStrictDecorator(unittest.TestCase):
    def test_valid_arguments(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(10, 5), 15)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
        with self.assertRaises(TypeError):
            sum_two("1", 2)


if __name__ == '__main__':
    unittest.main()
