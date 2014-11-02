from unittest import TestCase

from lesson5.Nesting import solution


class BracketsTestCase(TestCase):
    def test(self):
        self.assertEqual(1, solution('(()(())())'))
        self.assertEqual(0, solution('())'))
        self.assertEqual(0, solution('))(('))
        self.assertEqual(1, solution(''))
        self.assertEqual(1, solution('()(()())((()())(()()))'))
        self.assertEqual(0, solution('())(()'))