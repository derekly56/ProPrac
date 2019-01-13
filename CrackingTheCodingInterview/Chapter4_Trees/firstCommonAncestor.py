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

'''
Function firstCommonAncestor
----------------------------

This function will pass in a root and two nodes to check for where their first
common ancestor is located at. The solution is to use a recursive approach to
find the two nodes. Once the nodes are located, send back the value of 1. Since
there are two nodes, the combined value needs to be 2. Once 2 is reached at a
parent node, we know that the current node must be the first ancestor since it's
subtrees are returning values of 1 from each side or 2 from the same side.

Run-Time Complexity: O(n) 
'''
def firstCommonAncestor(root, nodeA, nodeB):
    if not root:
        return 0

    count = 0

    count += firstCommonAncestor(root.left, nodeA, nodeB)
    count += firstCommonAncestor(root.right, nodeA, nodeB)

    if count == 2:
        return root

    if root == nodeA or root == nodeB:
        count += 1

    return count


'''
Test cases
'''

treeOne = BST()
treeOne.insert(10)
treeOne.insert(5)
treeOne.insert(12)
treeOne.insert(4)
treeOne.insert(8)
treeOne.insert(13)

'''
Test 1
-------
This test will test for when they are both on opposite subtrees

nodeA = 5
nodeB = 13

Returned node should be 10
'''
nodeA = treeOne.root.left
nodeB = treeOne.root.right.right

print(nodeA.val)
print(nodeB.val)

test = firstCommonAncestor(treeOne.root, nodeA, nodeB)
print(test.val)

print()
print()

'''
Test 2
-------
This test will test for when they are both on the same subtrees

nodeC = 12
nodeD = 13

Returned node should be 10
'''
treeTwo = BST()
treeTwo.insert(10)
treeTwo.insert(5)
treeTwo.insert(12)
treeTwo.insert(4)
treeTwo.insert(8)
treeTwo.insert(13)

nodeC = treeTwo.root.right
nodeD = treeTwo.root.right.right

print(nodeC.val)
print(nodeD.val)

testTwo = firstCommonAncestor(treeTwo.root, nodeC, nodeD)
print(testTwo.val)
