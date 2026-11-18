import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4, 2), 0.5)
        self.assertEqual(div(-5, 10), -2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(3, 81), 4)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -8)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()