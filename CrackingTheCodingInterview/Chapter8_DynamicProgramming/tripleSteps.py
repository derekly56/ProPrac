'''
Author: Derek Ly
Question: Triple Steps (Pg. 134)

---------------------------------------------------------------------
A child is running up a staircase with n steps and can hop either
1,2,3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
---------------------------------------------------------------------
'''

'''
Function tripleSteps:
---------------------

This function will take in the number of steps and recursively build the solution
bottom-up DP. The function will test out all possible methods to either subtract
1, 2, or 3 steps in different combinations. When there is nothing left to subtract,
then we must have reached the "bottom". Once we reach the "bottom", we can return
1, because we know that this must've been 1 path to reach that bottom.

***
I am still working on using other types of solutions, such as memoization
(if possible)
***
'''

def tripleSteps(n):
    if n == 0:
        return 1

    steps = 0

    if n > 2:
        steps += tripleSteps(n - 3)

    if n > 1:
        steps += tripleSteps(n - 2)

    if n > 0:
        steps += tripleSteps(n - 1)

    return steps

total = tripleSteps(4)
print(total)
