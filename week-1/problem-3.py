"""Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head."""

# initialise variable to be returned for final answer
# 1. Need to iterate through characters in string
# test required to check if going in forward way through alphabet
# 2. when no longer going in alphabetical order - reset the index marker
# compare order of strings
# 3. if new strong longer than current string then overwrite it
# 4. store len(temporary string) as longest_string marker
# 5. search from new index marker to find next longest substring,
# 6. print final output

# starting string
s = 'azcbobobegghakl'

sub = longest = s[0]
# two strings equal to first character

for char in range(len(s)-1):
    if s[char+1] >= s[char]:  # compares next character to current character
        sub += s[char+1]
    else:
        sub = s[char+1]  # restarts substring with next character
    if len(sub) > len(longest):  # compares longest string to current string
        longest = sub

print('Longest substring in alphabetical order is: ' + str(longest))

