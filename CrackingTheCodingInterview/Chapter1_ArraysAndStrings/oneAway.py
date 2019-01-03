'''
Author: Derek Ly
Question: One Away (Pg. 91)
---------------------------------------------------------------------
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one (or zero)
edits away.

Example
-------

Pale -> Bale : True
Kale -> Bale : True
Pale -> Bake : False
Pale -> Bakers : False
---------------------------------------------------------------------
'''

'''
Function oneAway
----------------

This function will take in two strings and check if they are within 1 (or 0)
edits away from each other. If the length of the two strings differ by 2 or more,
then it automatically fails since it requires more than 1 edit. We then input
the frequency of s1's characters into a dictionary. Then, we will iterate through
s2's character frequencies and subtract that from the dictionary. If the remaining
values in the dictionary total 1 or less, then we know that the two strings are
indeed 1 edit away from each other. Otherwise, they are NOT.

Run-Time Complexity: O(n)
'''

def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    seen = {}

    for ch in s1:
        if ch in seen:
            seen[ch] += 1
        else:
            seen[ch] = 1

    for chr in s2:
        if chr in seen:
            seen[chr] -= 1

    total = 0
    for key, val in seen.items():
        if val > 0:
            total += val

    if total > 1:
        return False
    else:
        return True

'''
Test Cases
'''

'''
This first test case will pass
'''
x = "Pale"
y = "Bale"
print(oneAway(x,y))

'''
This second test case will fail
'''

s1 = "Pale"
s2 = "Bake"
print(oneAway(s1, s2))
