class node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            temp = node()
            temp.data = data
            self.head = temp
        else:
            t = self.head
            while(t.next is not None):
                t = t.next

            temp = node()
            temp.data = data
            t.next = temp
            temp.prev = t

def printll(head):
	t = head

	while(t.next != None):
		print(t.data, end = " ")
		t = t.next
	print(t.data)

	while(t):
		print(t.data, end = " ")
		t = t.prev

	print()


def consecutive(arr):
	blocks = 0
	blockSet = set()

	for i in range(len(arr)):
		cur = arr[i]
		blocks += 1

		if(cur.prev in blockSet):
			blocks -= 1

		if(cur.next in blockSet):
			blocks -=1

		blockSet.add(cur)

	return blocks

headOne = LinkedList()
headOne.insert(1)
headOne.insert(2)
headOne.insert(3)
headOne.insert(4)
headOne.insert(5)
headOne.insert(6)
headOne.insert(7)

arr = []
arr.append(headOne.head)
arr.append(headOne.head.next.next)
arr.append(headOne.head.next.next.next)
arr.append(headOne.head.next.next.next.next)

b = consecutive(arr)
print(b)
