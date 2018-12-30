import queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            t = Node(val)
            self.root = t
        else:
            t = self.root
            temp = Node(val)

            while(t):
                if t.data > val:
                    if t.left is None:
                        t.left = temp
                        break
                    else:
                        t = t.left
                elif t.data < val:
                    if t.right is None:
                        t.right = temp
                        break
                    else:
                        t = t.right
                else:
                    break

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data))
        inorder(root.right)

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
        print(str(root.data), end = " ")
    else:
        printLevel(root.left, i - 1)
        printLevel(root.right, i - 1)


def printBFSFunc(root):
    h = height(root)

    for i in range(h + 1):
        printLevel(root, i)
    print()

arr = []
def calculateAvg(root):
    sum = 0

    if root:
        a = calculateAvg(root.left)
        b = calculateAvg(root.right)
        sum = a + b + root.data

    return sum

def traverse(root):
    if root:
        global arr
        avg = calculateAvg(root)
        arr.append(avg)
        traverse(root.left)
        traverse(root.right)

def printBFSQueue(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data, end = " ")
        n = queue.pop(0)

        if n.left is not None:
            queue.append(n.left)

        if n.right is not None:
            queue.append(n.right)

    print()

tree = BST()
tree.insert(10)
tree.insert(12)
tree.insert(11)
tree.insert(4)
tree.insert(1)
tree.insert(6)
#inorder(tree.root)
#printBFSFunc(tree.root)
#printBFSQueue(tree.root)

traverse(tree.root)
print(arr)
