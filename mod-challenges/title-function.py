# Make function that replicates functionality of built in python string function.title()
# Idea created on beginner programmers discord
# by MajorDiscord and Fisk, Unit tests by Shiftypanda
from unittest import TestCase


s = 'we lOve to hAVe really amazingly Neat titles'

def convert_string_to_title(s):
    """
    :param s: string of any length
    :return: capitlised string with first letter in uppercase, rest letters in lower case.
    """



# Define tests

class TestTitleFunction(TestCase):

    def test_converts_to_title(self):
        s = 'we lOve to hAVe really amazingly Neat titles'
        response = convert_string_to_title(s)
        expected_response = s.title()
        self.assertEqual(expected_response, response)\

    def test_converts_including_question_mark(self):
        s = 'may the fOrTh be with you - obi?wan kenobi'
        response = convert_string_to_title(s)
        expected_response = s.title()
        self.assertEqual(expected_response, response)

    def test_converts_including_random(self):
        s = "that's the beSt damn españOl lesson I've #seenthisweek"
        response = convert_string_to_title(s)
        expected_response = s.title()
        self.assertEqual(expected_response, response)

    def test_converts_accents(self):
        s = "él ñiño"
        response = convert_string_to_title(s)
        expected_response = s.title()
        self.assertEqual(expected_response, response)

    def test_ignores_symbols(self):
        s = "@#%@$%.foo ?BAR ,bAZ"
        response = convert_string_to_title(s)
        expected_response = s.title()
        self.assertEqual(expected_response, response)