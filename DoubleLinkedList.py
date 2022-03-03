class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverseList(self):
        prev = None
        current = self.head
        while current:
            Next = current.next
            current.next = prev
            current.prev = Next
            prev = current
            current = Next
        self.head = prev


def sortedInsert(head,data):
    
    newNode = Node(data)
    if head is None:
        head = newNode
        return head

    if data <= head.data:
        newNode.next = head
        head.prev = newNode
        head = newNode
        return head

    current = head
    temp = None
    prev = None
    while current and current.data < data:
        prev = current.prev
        current = current.next
    if current is None:
        prev = prev.next
        newNode.prev = prev
        prev.next = newNode
        return head
    temp = current.prev
    temp.next = newNode
    newNode.prev = temp
    newNode.next = current
    current.prev = newNode
    
    return head
def printList(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
l = DLL()
l.push(4)
l.push(3)
l.push(2)

# l.reverseList()
l.printList()
