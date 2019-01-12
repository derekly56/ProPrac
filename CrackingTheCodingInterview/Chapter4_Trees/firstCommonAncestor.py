'''
Author: Derek Ly
Question: First Common Ancestor (Pg. 110)
---------------------------------------------------------------------
Design an algorithm and write code to find the first common ancestor
of two nodes in a binaray tree. Avoid storing additional nodes in a
data structure. NOTE: This is not necessarily a binary search tree.
---------------------------------------------------------------------
'''

'''
Standard Node / BST class
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

def firstCommonAncestor(root, nodeA, nodeB, count):
    if not root:
        return 0

    if count == 2:
        return root

    l = firstCommonAncestor(root.left, nodeA, nodeB, count)
    r = firstCommonAncestor(root.right, nodeA, nodeB, count)

    if root == nodeA or root == nodeB:
        count += 1
