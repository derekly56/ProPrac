'''
Author: Derek Ly
Question: Minimal Tree (Pg. 109)
---------------------------------------------------------------------
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a BST with minimal height
---------------------------------------------------------------------
'''

testArr = [1,2,3,4,5,6,7,8,9,10]

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

    def createMinimal(self, arr):
        if len(arr) >= 1:
            mid = len(arr) // 2
            self.insert(arr[mid])
            self.createMinimal(arr[0:mid])
            self.createMinimal(arr[(mid + 1):])

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

treeOne = BST()
treeOne.createMinimal(testArr)
printTree(treeOne.root)
print()
printBFSFunc(treeOne.root)
