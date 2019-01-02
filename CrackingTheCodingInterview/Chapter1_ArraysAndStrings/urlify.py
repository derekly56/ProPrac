'''
Author: Derek Ly
Question: URLify (Pg. 90)
---------------------------------------------------------------------
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

Example
-------

Input: "Mr John Smith"
Output: "Mr%20John%20Smith"
---------------------------------------------------------------------
'''

'''
Function urlify
---------------

This function will take in a string and find all empty spaces. The function will
create a new string and iterate backwards of the passed in string to copy and
replace the neccessary operations. If there is a space detected, then insert
'%20' into the empty space.

The reason why we are going backwards is because it is easier to insert it
into a new string, rather than overwrite the previous string. If we decided to
insert while traversing forward from the initial string, we would have to
constantly shift down 2 more spaces for the %20 to fit.

Run-Time Complexity: O(n)
'''

def urlify(s1):
    spaces = 0

    for ch in s1:
        if ch == ' ':
            spaces += 1

    newS = ""

    for i in range(len(s1) - 1, -1, -1):
        if s1[i] == ' ':
            newS = '%20' + newS
        else:
            newS = s1[i] + newS

    return newS

'''
Test Cases
'''

'''
This test case will return:

Mr%20John%20Smith
'''

x = "Mr John Smith"
y = urlify(x)
print(y)
