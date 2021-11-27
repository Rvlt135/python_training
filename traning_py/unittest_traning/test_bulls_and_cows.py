import unittest
from unittest import TestCase
from BullsAndCows import game


class TestBullsAndCowPositive(TestCase):
    def test_win(self):
        self.assertEqual(game(3207, 3207), "Вы выйграли!")

    def test_smoke_return_bulls(self):
        self.assertEqual(game(3207, 3217), "0 коровы, 3 быка")

    def test_smoke_return_cows(self):
        self.assertEqual(game(3207, 7123), "3 коровы, 0 быка")

    def test_smoke_return_unity_bulls_cows(self):
        self.assertEqual(game(3207, 3271), "1 коровы, 2 быка")

    def test_number_more_four(self):
        self.assertEqual(game(3207, 32711), "Значение < 5 символов")

    def test_no_matches(self):
        self.assertEqual(game(3207, 1456), "Нет совпадений")

    def test_string(self):  # ОК так как приводим все к строке в логике
        self.assertEqual(game(3207, "string"), "Нет совпадений")

    @unittest.skip("finalize validation number < 4")
    def test_number_less_four(self):
        self.assertEqual(game(3207, 32), "У вас число < 4-го")

    @unittest.skip("finalize empty line")
    def test_number_less_null(self):
        self.assertEqual(game(3207, ), "У вас число < 4-го")

    def test_repeat_number(self):
        self.assertEqual(game(3207, 3322), "Числа не должны повторяться!")

    @unittest.expectedFailure
    def test_space_number(self):
        self.assertEqual(game(3207, 0), """string index out of range""")
