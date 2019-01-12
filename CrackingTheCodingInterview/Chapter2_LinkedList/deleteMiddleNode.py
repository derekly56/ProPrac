'''
Author: Derek Ly
Question: Delete Middle Node (Pg. 94)
---------------------------------------------------------------------
Implement an algorithm to delete a node in the middle (not the
first/last, but not necessarily the middle) of a singly linked list,
given only access to that node.

Example
--------

Input: a -> b -> c -> d -> e -> f           , given node c
Output: a - >b -> d -> e -> f
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
Function deleteMiddleNode
-------------------------

This function will give a specific node to start at. The goal is to "delete" that
middle node. Since it is a singly linked list and we CANNOT iterate through
the list to find the next node, we just need to figure out where the given node
is pointing. The solution would be to force the current node to copy the contents
of the node next to it. This "deletes" the current node by forcing it to be it's
neighbors

Run-Time Complexity: O(1)
'''

def deleteMiddleNode(nodeA):
    if nodeA.next is None:
        return

    temp = nodeA.next
    nodeA.data = temp.data
    nodeA.next = temp.next

def printList(head):
    t = head

    while t:
        print(t.data, end = " ")
        t = t.next

    print()
'''
Test Cases
'''

'''
Given Node at C
'''
headOne = LinkedList()
headOne.insert('A')
headOne.insert('B')
headOne.insert('C')
headOne.insert('D')
headOne.insert('E')
headOne.insert('F')

printList(headOne.head)
deleteMiddleNode(headOne.head.next.next)
printList(headOne.head)
