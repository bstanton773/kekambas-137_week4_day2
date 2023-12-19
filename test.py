from unittest import TestCase

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_one(self):
        self.assertEqual(solution("test"), "e")
    def test_example_two(self):
        self.assertEqual(solution("teeter"), "r")
    def test_example_three(self):
        self.assertEqual(solution("trend"), "t")
    def test_example_four(self):
        self.assertEqual(solution("aabbcc"), None)
