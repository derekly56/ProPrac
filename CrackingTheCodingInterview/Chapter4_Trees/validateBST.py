'''
Author: Derek Ly
Question: Validate BST (Pg. 110)
---------------------------------------------------------------------
Implement a function to check if a binary tree is a binary search tree.
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

status = True

'''
Function validateBST
--------------------

This function will check a binary tree to see if it is a binary search tree (BST).
We will use a global variable to store the status of the tree. If any conditions
fail, then the status will return false and not continue with the tree.

Run-Time Complexity: O(n)
'''
def validateBST(root):
    global status
    if root:
        if root.left is not None and root.right is not None:
            if root.left.val < root.val and root.val < root.right.val:
                validateBST(root.left)
                validateBST(root.right)
            else:
                status = False
        elif root.left is None and root.right is not None:
            if root.val < root.right.val:
                validateBST(root.right)
            else:
                status = False
        elif root.left is not None and root.right is None:
            if root.left.val < root.val:
                validateBST(root.left)
            else:
                status = False

'''
Test Cases
'''

'''
This first tree will yield true

root: 6
1st level: 4 9
2nd level: 2 5 8 10
'''
treeOne = BST()
treeOne.insert(6)
treeOne.insert(4)
treeOne.insert(5)
treeOne.insert(2)
treeOne.insert(9)
treeOne.insert(8)
treeOne.insert(10)
validateBST(treeOne.root)
print(status)

'''
This second tree will yield False

root: 6
1st level: 4 9
2nd level: 2 3 8 10

We will purposefully add a node of value 3 to 4's right child, causing it to
fail the BST conditions
'''

treeTwo = BST()
treeTwo.insert(6)
treeTwo.insert(4)
treeTwo.insert(2)
treeTwo.insert(9)
treeTwo.insert(8)
treeTwo.insert(10)
# Adding in value 3 into the wrong spot
treeTwo.root.left.right = Node(3)
validateBST(treeTwo.root)
print(status)
