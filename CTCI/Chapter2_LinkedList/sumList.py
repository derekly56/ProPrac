class node:
    def __init__(self):
        self.data = None
        self.next = None

def insert(head, data):
    if head is None:
        temp = node()
        temp.data = data
        head = temp
    else:
        t = head
        while(t.next is not None):
            t = t.next

        temp = node()
        temp.data = data
        t.next = temp

def sumList(h1, h2):

    tens = 0
    totalOne = 0
    while(h1):
        totalOne += (h1.data * (10**tens))
        tens += 1
        h1 = h1.next

    tens2 = 0
    totalTwo = 0
    while(h2):
        totalTwo += (h2.data * (10**tens2))
        tens2 += 1
        h2 = h2.next

    newTotal = totalOne + totalTwo

    newList = node()
    t = newList
    while(newTotal > 0):
        rem = newTotal % 10

        if t is None:
            temp = node()
            temp.data = rem
            t = temp
        else:
            temp = node()
            temp.data = rem

            t.next = temp
            t = t.next

        newTotal = newTotal // 10

    return newList

head1 = node()
insert(head1, 5)
insert(head1, 9)
insert(head1, 2)

head2 = node()
insert(head2, 7)
insert(head2, 1)
insert(head2, 6)

while(head1):
    print(str(head1.data))
    head1 = head1.next

'''
newList = sumList(head1, head2)

while(newList):
    print(str(newList.data), end = " ")
    newList = newList.next
print()
'''
