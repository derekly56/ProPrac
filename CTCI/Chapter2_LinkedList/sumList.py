'''
Author: Derek Ly
Question: Sum Lists(Pg. 95)
---------------------------------------------------------------------
You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order, such
that the 1's digit is at the head of the list. Write a function that
adds the two numbers and returns the sum as a linked list.

Example(s)
--------
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) = 617 + 295
Output: (2 -> 1 -> 9) = 912
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
Function sumList:
-----------------
sumList will take two linked list heads and returns a new linked list
that will contain the new total sum in the correct order
'''
def sumList(h1, h2):

    tens = 0
    totalOne = 0
    while(h1):
        totalOne += (h1.data * (10**tens))
        tens += 1
        h1 = h1.next

    tens2 = 0
    totalTwo = 0
    while(h2):
        totalTwo += (h2.data * (10**tens2))
        tens2 += 1
        h2 = h2.next

    newTotal = totalOne + totalTwo

    newList = LinkedList()

    while(newTotal > 0):
        rem = newTotal % 10
        newList.insert(rem)

        newTotal = newTotal // 10

    return newList

'''
Function printList:
-------------------
This function will print out the linkedlist and display
'''
def printList(head):
    while(head):
        print(str(head.data), end = " ")
        head = head.next
    print()

# Test cases
head1 = LinkedList()
head1.insert(5)
head1.insert(9)
head1.insert(2)

head2 = LinkedList()
head2.insert(7)
head2.insert(1)
head2.insert(6)

head3 = sumList(head1.head, head2.head)
printList(head3.head)
