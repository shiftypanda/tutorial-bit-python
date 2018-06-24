"""Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head."""

# starting string
s = 'azcbobobegghakl'

# initialise variable to be returned for final answer
longest_substring = ""
start_index = 0
# 1. Need to iterate through characters in string
for char in s:
    start_index += 1
    new_substring = s[start_index:]
# test required to check if going in forward way through alphabet
    if char in "abcdefghijklmnopqrstuvwxyz":
        longest_substring.append(char)

# 2. when no longer going in alphabetical order - reset the index marker

# 3. if new strong longer than current string then overwrite it
# 4. store len(temporary string) as longset_string marker
# 5. search from new index marker to find next longest substring,
# 6. print final output



print("Longest substring in alphabetical order is: " + str(len(longest_substring)))