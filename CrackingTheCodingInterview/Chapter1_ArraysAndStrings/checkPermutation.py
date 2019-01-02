'''
Author: Derek Ly
Question: Check Permutation(Pg. 90)
---------------------------------------------------------------------
Given two strings, write a method to decide if one is a permutation
of the other.
---------------------------------------------------------------------
'''

'''
Function checkPermutation
-------------------------

This function will take in two strings and compare for permutations. If they
are not of the same length, then return False since it isn't possible. The
function will create a dictionary to store iterations of characters that have
been seen in s1. Then, go through characters in string 2 and decrement those
values from s1 in in the dictionary. At the very end, iterate through the
dictionary for values. If the two strings are permutations of one another, then
every value in the dictionary will be 0, if they are different, then return False

Run-Time Complexity: O(n)

This function will utilize uppercase and lowercase as their own unique characters.
However, one could simply force the two strings to be inputted as lowercase,
and then the function would still work the same.
'''

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    permutation = {}

    for ch in s1:
        if ch in permutation:
            permutation[ch] += 1
        else:
            permutation[ch] = 1

    for chr in s2:
        if chr in permutation:
            permutation[chr] -= 1
            if permutation[chr] == 0:
                del permutation[chr]

    total = 0
    for key, val in permutation.items():
        if val > 0:
            total += val

    if total == 0:
        return True
    else:
        return False

'''
Test cases
'''

'''
This first test case will return True
'''

s1 = "tacocat"
s2 = "atcocta"

x = checkPermutation(s1, s2)
print(x)

'''
This second test case will return False
'''
s3 = "Chicken"
s4 = "Chickea"

y = checkPermutation(s3, s4)
print(y)
