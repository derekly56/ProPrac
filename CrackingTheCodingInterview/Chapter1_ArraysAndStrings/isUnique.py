'''
Author: Derek Ly
Question: Is Unique(Pg. 90)
---------------------------------------------------------------------
Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
---------------------------------------------------------------------
'''

'''
Function isUnique
-----------------
Run-Time Complexity: O(n)

This function will take in a string and iterate through every character
in that string. We will also make a dictionary to store characters that
have already been seen. If it is already seen, then we know that it is a
repeat character. If we go through the entire string, then the string must've
had all unique characters since none of them were flagged as a reoccurrence.

In the case that we CANNOT use an additional data structure, then a method
would be to sort the string. Once it is sorted, we can check in a linear
fashion of any repeats. This would run in O(nlogn).

Finally, we can use a brute force method where we iterate through the entire
string checking for repeats of each character. This would run in O(n^2).

As always, check with the interviewer what your restrictions are.
'''

def isUnique(s):
    seen = {}

    for ch in s:
        if ch in seen:
            return False

        seen[ch] = 1

    return True

'''
Test cases
'''
s = "abcdef"
t = "abcdea"

print(isUnique(s)) # Should return True
print(isUnique(t)) # Should return False
