"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2"""
print("attempting problem 2 using while loop")
s = "azcbobobegghakl"
bob_occurances = 0
increments = 0
while increments <= len(s):
    temp = s[increments : (increments+3)]
    if "bob" == temp:
        bob_occurances += 1
    increments += 1

print("Number of times bob occurs is: " + str(bob_occurances))

# logic
# 1. aim - search within string for matching characters
# 2. for each matching substring add increment using slicing and incrementing on 3 letters

s = "azcbobobegghakl"
bob_occurances = 0

for char in s:
    location = s.
    temp = s[location : (location+3)]
    if "bob" == temp:
        bob_occurances += 1


print("Number of times bob occurs is: " + str(bob_occurances))
s