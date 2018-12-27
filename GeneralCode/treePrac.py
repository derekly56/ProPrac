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

def printBFS(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data)

        n = queue.pop(0)

        if n.left is not None:
            queue.append(n.left)

        if n.right is not None:
            queue.append(n.right)

tree = BST()
tree.insert(10)
tree.insert(12)
tree.insert(11)
tree.insert(4)
tree.insert(1)
tree.insert(6)
#inorder(tree.root)
printBFS(tree.root)
