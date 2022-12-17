from unittest import TestCase
from client import getRatio


class Test(TestCase):
    def test_get_ratio_b0(self):
        # Test O division Case
        actual = getRatio(1, 0)
        expected = None
        self.assertEqual(actual, expected)

    def test_get_ratio_agtb(self):
        # Test O division Case
        actual = getRatio(100, 50)
        expected = 2
        self.assertEqual(actual, expected)

    def test_get_ratio_bgta(self):
        # Test O division Case
        actual = getRatio(10, 75)
        expected = .13333
        self.assertAlmostEqual(actual, expected, 5)
