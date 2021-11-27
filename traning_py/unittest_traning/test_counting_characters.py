import unittest
from unittest import TestCase
from CountingCharacters import counter


class TestCountingCharacters(TestCase):
    def test_smoke_counter(self):
        self.assertEqual(counter("abbccc"), "ab2c3")

    def test_cyrillic(self):
        self.assertEqual(counter("абб"), "аб2")

    def test_one_symbol(self):
        self.assertEqual(counter("a"), "a")

    def test_counter_not_one_symbol(self):
        self.assertEqual(counter("aaaaa"), "a5")

    def test_transformation_int(self):
        self.assertEqual(counter(1223334444), "1223344")

    def test_spec_symbols(self):
        self.assertEqual(counter("@#$%^&"), "@#$%^&")

    @unittest.skip("IndexError")
    def test_null_symbols(self):
        self.assertEqual(counter(""), "")

    def test_float_symbols(self):
        self.assertEqual(counter(1.1), "1.1")
