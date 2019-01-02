'''
Author: Derek Ly
Question: Check Balanced (Pg. 110)
---------------------------------------------------------------------
Implement a function to check if a binary tree is balanced. For the
purposes of this question, a balanced tree is defined to be a tree
such that that heights of the two subtrees of any node never differ
by more than one.
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

def height(root):
    if root is None:
        return 0
    else:
        l = height(root.left)
        r = height(root.right)

        return(max(l, r) + 1)

'''
Function checkBalanced
----------------------

This function will iterate through every node in the binary tree and check
it's two subtrees for equality in heights (i.e within 1 of each other). If
the two are within reasonable range (difference of 1), then continue traversing,
else mark the global marker as False and stop.

We are also using a helper function height to determine the height of any given
binary tree.

Run-Time Complexity: O(n)
'''
status = True

def checkBalanced(root):
    global status
    if root:
        l = height(root.left)
        r = height(root.right)

        if abs(l - r) >= 2:
            status = False
        else:
            checkBalanced(root.left)
            checkBalanced(root.right)

'''
Test Cases
'''

'''
Treeone should return True since every subtree is leveled
'''
treeOne = BST()
treeOne.insert(6)
treeOne.insert(4)
treeOne.insert(5)
treeOne.insert(2)
treeOne.insert(9)
treeOne.insert(8)
treeOne.insert(10)
checkBalanced(treeOne.root)
print(status)


'''
Treetwo should return False since one level is 2 heights higher
'''

treeTwo = BST()
treeTwo.insert(6)
treeTwo.insert(4)
treeTwo.insert(5)
treeTwo.insert(3)
treeTwo.insert(2)
treeTwo.insert(1)
treeTwo.insert(9)
treeTwo.insert(8)
treeTwo.insert(10)
checkBalanced(treeTwo.root)
print(status)
