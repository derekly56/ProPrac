'''
Author: Derek Ly
Question: Successor (Pg. 110)
---------------------------------------------------------------------
Write an algorithm to find the "next" node (i.e in-order successor)
of a given node in a binary search tree. You may assume that each
node has a link to its parent.
---------------------------------------------------------------------
'''

'''
Standard Node and BST class
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        t = self.root

        if t is None:
            temp = Node(val)
            self.root = temp
        else:
            while(t):
                if t.val < val:
                    if t.right is None:
                        temp = Node(val)
                        t.right = temp
                        break
                    else:
                        t = t.right
                elif t.val > val:
                    if t.left is None:
                        temp = Node(val)
                        t.left = temp
                        break
                    else:
                        t = t.left

'''
Function Successor
------------------

IN PROGRESS
'''
def successor(root, val):




'''
Test cases
'''

'''
In-order traversal of this will yield:
2 -> 4 -> 6 -> 8 -> 9 -> 10

So, if we wanted to find 6's successor, it would be 8
'''
treeOne = BST()
treeOne.insert(6)
treeOne.insert(4)
treeOne.insert(5)
treeOne.insert(2)
treeOne.insert(9)
treeOne.insert(8)
treeOne.insert(10)
