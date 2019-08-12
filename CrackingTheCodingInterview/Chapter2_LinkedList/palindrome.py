'''
Author: Derek Ly
Question: palindrome (Pg. 95)
---------------------------------------------------------------------
Implement a function to check if a linked list is a palindrome

Example
--------
Input: a -> b -> c -> d -> e -> f
Output: False

Input: a -> b -> c -> c -> b -> a
Output: True
---------------------------------------------------------------------
'''

'''
Standard Node / LinkedList classes
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            temp = node()
            temp.data = data
            self.head = temp
        else:
            t = self.head
            while(t.next is not None):
                t = t.next

            temp = node()
            temp.data = data
            t.next = temp

'''
Function palindrome
------------------

This will will give a specific node to start at (which is the head) and
then determine if the entire linked list is a palindrome. We can iterate
through this linkedlist to get the length and go towards the middle. We can
append every element onto a stack until we have reached the middle of the
linked list. From there, depending on if it's even or odd, we will pop
the current element on the stack to match with the following elements
remaining in the linked list. If at each pop it matches with the next element,
then the code will traverse through the linked list. If it doesn't match,
then we know we have a non-palindrome linked list since every element after
the middle element needs to be an exact match.

Run-Time Complexity: O(n)
Space Complexcity: O(n)
'''

def palindrome(l1):

	if l1 is None:
		return False

	if l1 != None and l1.next is None:
		return True

	pstack = []
	length = 1
	temp = l1

	# Find the length of the linked list
	while temp.next != None:
		temp = temp.next
		length += 1

	# If the linked list is even, check every element with each other
	# starting from the middle
	# Else, skip the middle element and check after the middle
	if length % 2 == 0:
		start = 0
		cursor = l1

		while(start != length/2):
			pstack.append(cursor.data)
			cursor = cursor.next
			start += 1

		while(cursor != None):
			top = pstack.pop()

			if top != cursor.data:
				return False

			cursor = cursor.next
	else:
		start = 0
		cursor = l1

		while(start != length//2):
			pstack.append(cursor.data)
			cursor = cursor.next
			start += 1

		cursor = cursor.next

		while(cursor != None):
			top = pstack.pop()

			if top != cursor.data:
				return False

			cursor = cursor.next

	return True

'''
Test 1
Input: a -> d -> c -> d -> a
Output: True
'''
headOne = LinkedList()
headOne.insert('a')
headOne.insert('d')
headOne.insert('c')
headOne.insert('d')
headOne.insert('a')

testOne = palindrome(headOne.head)
print(testOne)

'''
Test 2
Input: a -> d -> d -> d -> d -> a
Output: True
'''
headTwo = LinkedList()
headTwo.insert('a')
headTwo.insert('d')
headTwo.insert('d')
headTwo.insert('d')
headTwo.insert('d')
headTwo.insert('a')

testTwo = palindrome(headTwo.head)
print(testTwo)

'''
Test 3
Input: a -> d -> d -> d -> b
Output: False
'''
headThree = LinkedList()
headThree.insert('a')
headThree.insert('d')
headThree.insert('d')
headThree.insert('d')
headThree.insert('b')

testThree = palindrome(headThree.head)
print(testThree)
