'''
Author: Derek Ly
Question: Kth to last (Pg. 94)
---------------------------------------------------------------------
Implement an algorithm to find the kth to last element of a singly
linked list.

Example
--------

Input: 10 -> 7 -> 11 -> 3 -> 2                   k = 2
Output: 11
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

def kthToLast(head, k):
    if not head:
        return

    length = 0

    t = head

    while t:
        length += 1
        t = t.next

    jump = (length - k) - 1

    temp = head
    while jump > 0:
        temp = temp.next
        jump -= 1

    print(temp.data)


'''
Test cases
'''

headOne = LinkedList()
headOne.insert(10)
headOne.insert(7)
headOne.insert(11)
headOne.insert(13)
headOne.insert(12)

kthToLast(headOne.head, 2)
