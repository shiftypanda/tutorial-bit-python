"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl',

your program should print:

Number of vowels: 5
"""

import unittest
from unittest import TestCase
from unittest import skip

def check_vowel(character):
    """checks if passed character is a vowel"""
    if character == "a":
        response = True
    elif character == "e":
        response = True
    elif character == "i":
        response = True
    elif character == "o":
        response = True
    elif character == "u":
        response = True

    else:
        response = False

    return response

def count_vowels_in_string(s):
    """ counts and increments for vowels in a string"""
    total_vowels = 0
    for character in s:
        if check_vowel(character) == True:
            total_vowels += 1
    return "Number of vowels: " + str(total_vowels)

#count_vowels_in_string(s)

#redefined to one code string
s = "azcbobobegghakl"
total_vowels = 0
for character in s:
    if character == "a":
        total_vowels += 1
    elif character == "e":
        total_vowels += 1
    elif character == "i":
        total_vowels += 1
    elif character == "o":
        total_vowels += 1
    elif character == "u":
        total_vowels += 1
print("Number of vowels: " + str(total_vowels))


class TestProblemOne(TestCase):


    def test_correct_output(self):
        s = "azcbobobegghakl"
        response = count_vowels_in_string(s)
        self.assertEqual(response, "Number of vowels: 5")

    def test_random_long_string_output(self):
        s = "assdfkjnsisdfdsekjnkjnokjnkjukjnkjnukjnkjnakjnkjnekjnkni"
        response = count_vowels_in_string(s)
        self.assertEqual(response, "Number of vowels: 9")

    def test_check_vowel_returns_true_if_vowel_a(self):
        correct_vowel = "a"
        response = check_vowel(correct_vowel)
        self.assertTrue(response)

    def test_check_vowel_returns_true_if_vowel_e(self):
        correct_vowel = "e"
        response = check_vowel(correct_vowel)
        self.assertTrue(response)

    def test_check_vowel_returns_true_if_vowel_i(self):
        correct_vowel = "i"
        response = check_vowel(correct_vowel)
        self.assertTrue(response)

    def test_check_vowel_returns_true_if_vowel_o(self):
        correct_vowel = "o"
        response = check_vowel(correct_vowel)
        self.assertTrue(response)

    def test_check_vowel_returns_true_if_vowel_u(self):
        correct_vowel = "u"
        response = check_vowel(correct_vowel)
        self.assertTrue(response)


    def test_check_vowel_returns_true_if_not_vowel_c(self):
        wrong_vowel = "c"
        response = check_vowel(wrong_vowel)
        self.assertFalse(response)


