# We can use the idea of bisection search to determine if a character is in a string,
# so long as the string is sorted in alphabetical order.
#
# First,
# test the middle character of a string against the character you're looking for (the "test character").
# If they are the same,
# we are done - we've found the character we're looking for!
#
# If they're not the same,
# check if the test character is "smaller" than the middle character.
# If so,
# we need only consider the lower half of the string;
# otherwise,
# we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)
#
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
# char will be a single character and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.
#
# As you design the function,
# think very carefully about what the base cases should be.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # check base case if empty string return false
    if aStr == '':
        False

    # if string length one check if character is the one we want
    if len(aStr) == 1:
        return aStr == char

    # Base case: see if character is in the middle of test case
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]

    if char == midChar:
        # char found
        return True

    # recursive case: if the test character is is smaller then recursively search
    # first half of string using bisection
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # otherwise the test character is larger so recursively search last half
    else:
        return isIn(char, aStr[midIndex+1:])


def isIn_first_go(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    NOTE: didnt read it tried to make implemeationt to alpabestise the string..
    '''
    # sort string first using a for loop, if c ? tower of hanoi type solution
    def sort_string(aStr):
        """
        :param aStr:
        :return: string sorted alphanumerically returned as lowercase
        """

        s = aStr.lower()
        sub_string = ""
        if len(s) == 1:
            return s
        if s == '':
            return ValueError("empty string given")
        else:
            for char in range(len(s)-1):
                if s[char+1] >= s[char]:
                    sub_string += s[char+1]
            return sub_string
        return sub_string

    # slice string starting from len(aStr)/2
    def bisect_string(aStr):
        return sort_string(aStr[len(aStr)//2])


    # empty string
    if aStr == '':
        pass

    # string length 1
    if len(aStr) == 1:
        pass
    # test character equals middle character


    # recurisve function
    print(str(sort_string(aStr)))
    print(str(bisect_string(sort_string(aStr))))
    return sort_string(aStr)

isIn('a', 'sldsjflksjwefowbfoobalskdfjdsl')