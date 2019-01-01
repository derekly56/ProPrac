'''
Author: Derek Ly
Question: Minimal Tree (Pg. 109)
---------------------------------------------------------------------
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a BST with minimal height
---------------------------------------------------------------------
'''

'''
Standard Node / BST Class
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
    Function createMinimal
    ----------------------
    Run-Time Complexity: O(nlogn)

    This function will take in the sorted array and then insert the data
    in one at a time. The data will be inserted by the middle value of
    the array. Once the data is inserted, send in the left half to insert
    the next middle value. Then send in the right half of the array.

    The algorithm behind this is to create the smallest height tree as possible.
    This can only be done when everything to the left of the root and everything
    to the right of the root has the same amount of elements. This will ensure
    that we will be able to create a minimal height tree. If we were to just
    insert elements in as they are sorted, then we will have a tree that is of
    height n, where n is length of the array.

    '''
    def createMinimal(self, arr):
        if len(arr) >= 1:
            mid = len(arr) // 2
            self.insert(arr[mid])
            self.createMinimal(arr[0:mid])
            self.createMinimal(arr[(mid + 1):])

'''
These four helper functions below will print out the tree.

PrintTree will print the tree as an inorder Traversal, so the function will
return a sorted "list" since the array we are inputting is SORTED and is a BST

PrintBFSFunc will print the tree as a BFS method and print out each data node
at each level. Here we can check for the minimal tree
'''

def height(root):
    if root is None:
        return -1
    else:

        l = height(root.left)
        r = height(root.right)

        return(max(l,r) + 1)

def printLevel(root, i):
    if root is None:
        return

    if i == 0:
        print(str(root.val), end = " ")
    else:
        printLevel(root.left, i - 1)
        printLevel(root.right, i - 1)

def printBFSFunc(root):
    h = height(root)

    for i in range(h + 1):
        printLevel(root, i)
        print()
    print()

def printTree(root):
    if root:
        printTree(root.left)
        print(root.val, end = " ")
        printTree(root.right)

'''
Test cases
'''
testArr = [1,2,3,4,5,6,7,8,9,10]

treeOne = BST()
treeOne.createMinimal(testArr)
printTree(treeOne.root)
print()
printBFSFunc(treeOne.root)
