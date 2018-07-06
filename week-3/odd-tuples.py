# Write a procedure called oddTuples,
# which takes a tuple as input,
# and returns a new tuple as output,
# where every other element of the input tuple is copied,
# starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
# then evaluating oddTuples on this input
# would return the tuple ('I', 'a', 'tuple').


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # return original tuple sliced from beginning to end with skip every 2
    odd_tuples = aTup[::2]

    return odd_tuples

import unittest
from unittest import TestCase

class OddTuplesTest(TestCase):

    def test_I_am_a_test_tuple(self):
        response = oddTuples(('I', 'am', 'a', 'test', 'tuple'))
        self.assertEqual(('I', 'a', 'tuple'), response)

if __name__ == '__main__':
    unittest.main()