'''
Author: Derek Ly
Question: Remove Dups (Pg. 94)
---------------------------------------------------------------------
Write code to remove duplicates from an unsorted linked list
---------------------------------------------------------------------
'''

'''
Standard Node / LinkedList Class
'''
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            temp = Node(value)
            self.head = temp
        else:
            t = self.head

            while(t.next is not None):
                t = t.next

            temp = Node(value)
            t.next = temp

    '''
    Function removeDups
    -------------------
    Run-Time Complexity: O(n)

    This function will traverse the entire unsorted linkedlist and remove
    all duplicates. The function will store all unique keys into a dictionary
    and check all incoming nodes if there is already a match in the dictionary.

    If we are cannot use a temporary buffer (i.e additional data structures),
    then we can use to pointers and iterate through the linkedlist and check
    for repeats. This would be the brute force method and will run in O(n^2)

    As always, check with the interviewer.
    '''
    def removeDups(self):
        if self.head is None:
            return
        else:
            t = self.head
            s = self.head.next

            if s is None:
                return

            seen = {}
            seen[t.val] = 1

            while(s):
                if s.val in seen:
                    s = s.next
                    t.next = s
                else:
                    seen[s.val] = 1
                    s = s.next
                    t = t.next

'''
Helper function to print the current list
'''
def printList(head):
    while(head):
        print(str(head.val), end = " ")
        head = head.next
    print()

'''
Test cases
'''

listOne = LinkedList()
listOne.insert(2)
listOne.insert(1)
listOne.insert(5)
listOne.insert(3)
listOne.insert(2)
listOne.insert(5)

# This should produce: 2 1 5 3 2 5
printList(listOne.head)

listOne.removeDups()

# This should produce: 2 1 5 3
printList(listOne.head)
