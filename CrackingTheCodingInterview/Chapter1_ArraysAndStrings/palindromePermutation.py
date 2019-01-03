'''
Author: Derek Ly
Question: Palindrome Permutation (Pg. 91)
---------------------------------------------------------------------
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word of phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.

Example
-------

Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta")
---------------------------------------------------------------------
'''

'''
Function palindromePermutation
------------------------------

This function will take in a string and remove all of the whitespaces and force
the characters to be lowercase. The function will then put all of the characters
into a dictionary to count it's frequency. For a palindrome to be effective, it
depends on the length of the string itself. If the string is of even length, then
we know that there needs to be ALL even pairs of letters. If the string is of odd
length, then we can only have 1 odd frequency and all even pairs. From there, we
can iterate through the dictionary, depending on the length of the string,
implement an algorithm to find either all pairs or 1 odd frequency.

Run-Time Complexity: O(n)

Example
-------

s1 = "AABB"
This works because since it is of even length, it has all even pairs
of characters frequency

s2 = "AAABBB"
This will not work because it is even length but has two odd frequencies



'''

def palindromePermutation(s1):
    st = s1.replace(' ', '')
    st = st.lower()

    perm = {}

    for ch in st:
        if ch in perm:
            perm[ch] += 1
        else:
            perm[ch] = 1

    if len(st) % 2 == 0:
        for key, val in perm.items():
            if val % 2 != 0:
                return False

        return True
    else:
        onePair = False

        for key, val in perm.items():
            if val % 2 != 0:
                if not onePair:
                    onePair = True
                else:
                    return False

        if onePair:
            return True
        else:
            return False

'''
Test Cases
'''

'''
This first test case will pass
'''
x = "Tact Coa"
print(palindromePermutation(x))

'''
This second test case will fail
'''

y = "Tact Coaa"
print(palindromePermutation(y))
