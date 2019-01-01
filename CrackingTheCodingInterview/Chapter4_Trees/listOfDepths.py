'''
Author: Derek Ly
Question: List of Depths (Pg. 109)
---------------------------------------------------------------------
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth (e.g if you have a tree with depth D,
you'll have D linked lists).
---------------------------------------------------------------------
'''

'''
Before we define any classes, be sure to ask the interviewer about what
type of tree they are expecting us to account for. While the code will
run the same for all the trees, it's good to get additional background
knowledge. Also, considering that it'll be an hour interview, you
probably won't have time to code up a perfect tree class, but it's good
to understand how to define it.
'''

'''
Standard Node / BST Class
Standard NodeLL / Linked List Class
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class NodeLL:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            temp = NodeLL(val)
            self.head = temp
        else:
            t = self.head

            while(t.next != None):
                t = t.next

            temp = NodeLL(val)
            t.next = temp

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
We will be using two helper functions:
1) height -> find height of tree
2) linkedListLevel -> traverse through tree and grab all nodes at that level
'''
def height(root):
    if root is None:
        return -1
    else:
        l = height(root.left)
        r = height(root.right)

        return(max(l, r) + 1)

def linkedListLevel(root, head, i):
    if root is None:
        return

    if i == 0:
        head.insert(root.val)
    else:
        linkedListLevel(root.left, head, i - 1)
        linkedListLevel(root.right, head, i - 1)

'''
Function listOfDepths
---------------------

This function will find the height of the given tree and create a list
to store the head of the linked lists. The function will iterate through
each level of the tree and create a linkedlist to store all the ndoes on
that level. Once it is done, the head of the linked list will be appended
to a list.

To check, we need a printDepths function to print out all of the contents. Each
position in the list represents the specific level.
(i.e depths[0] = root, depths[1] = 1st level, ...)

Run-Time Complexity: O(nlogn)
'''
def listOfDepths(root):
    h = height(root)
    depths = []

    for i in range(h + 1):
        temp = LinkedList()
        linkedListLevel(root, temp, i)
        depths.append(temp.head)

    return depths

def printDepths(depths):
    if depths is None:
        return
    else:
        for i in range(len(depths)):
            t = depths[i]

            while(t):
                print(str(t.val), end = " ")
                t = t.next

            print()

'''
Test cases
'''

'''
This tree will have 3 levels, so we should only see 3 linked lists

root - 6
1st level - 4 9
2nd level - 2 5 7 10
'''
treeOne = BST()
treeOne.insert(6)
treeOne.insert(4)
treeOne.insert(2)
treeOne.insert(5)
treeOne.insert(9)
treeOne.insert(7)
treeOne.insert(10)

arr = listOfDepths(treeOne.root)
printDepths(arr)
