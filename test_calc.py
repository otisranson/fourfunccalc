#!/usr/bin/env python
import unittest

import main


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)
        self.assertEqual(main.subtract(-1, 1), -2)
        self.assertEqual(main.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        self.assertEqual(main.multiply(-5, 5), -25)
        self.assertEqual(main.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(main.divide(18, 9), 2)
        self.assertEqual(main.divide(-18, 9), -2)
        self.assertEqual(main.divide(-1, -1), 1)
        self.assertRaises(ValueError, main.divide, 10, 0)


if __name__ == "__main__":
    unittest.main()
