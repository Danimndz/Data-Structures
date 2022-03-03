class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        auxNode = self.head
        while (auxNode.next != None):
            auxNode = auxNode.next

        auxNode.next = newNode

    def addNodeAtPos(self, data, position):
        newNode = Node(data)
        if position == 0:
            if self.head is None:
                self.head = newNode
                return
            newNode.next = self.head
            self.head = newNode
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        if temp.next is None:
            temp.next = newNode
        newNext = temp.next
        temp.next = newNode
        newNode.next = newNext

    def deleteNode(self, position):
        temp = self.head
        if self.head is None:
            return
        if position == 0:
            self.head = temp.next
            temp = None

        for i in range(position-1):
            temp = temp.next
            # print("debug1:",temp.data)
        nnext = temp.next
        # print("Borrar:",nnext.data)
        # Si es el ultimo
        if nnext.next is None:
            nnext = None
            temp.next = None
        else:
            newNext = nnext.next
            nnext = None
            temp.next = newNext

    def printList(self):
        auxNode = self.head
        while (auxNode != None):
            print(auxNode.data)
            auxNode = auxNode.next

    def reversePrint(self, head):
        if head is None:
            return
        else:
            self.reversePrint(self.head.next)
            print(self.head.data)

    def reverseList(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.head

        temp = self.head
        prev = None
        # 1->2->3->None
        while temp:
            Next = temp.next
            temp.next = prev
            prev = temp
            temp = Next
        self.head = prev


def reverseList(head: Node) -> Node:
    temp = head
    prev = None
    while temp:
        newNext = temp.next
        temp.next = prev
        prev = temp
        temp = newNext
    head = prev
    return head


def getNodeValueFromTail(head: Node, position: int) -> int:
    temp = head
    arr =[]
    while temp:
        arr.append(temp.data)
        temp = temp.next

    return arr[(len(arr)-1)-position]


def printList(head):
    auxNode = head
    while (auxNode != None):
        print(auxNode.data)
        auxNode = auxNode.next


def compareLists(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1:
        if temp1 == None:
            return 0
        if temp1.data != temp2.data:
            return 0
        temp1 = temp1.next
        temp2 = temp2.next
    if temp2 == None:
        return 0
    return 1


def mergeList(head1, head2):
    if head1.data < head2.data:
        current = head1
        temp = head2
    else:
        current = head2
        temp = head1
    newHead = current
    while (1):
        if current.next is None or current.next.data > temp.data:
            aux = current.next
            _temp = temp
            temp = temp.next  # avanzar
            current.next = _temp
            _temp.next = aux

        current = current.next
        if temp is None:
            break

    return newHead


def eliminateDuplicates(head):
    if head is None:
        return
    current = head
    while current:
        if current.next and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def isCycled(head):
    temp1 = head
    temp2 = head
    while temp1 and temp1.next:
        temp1 = temp1.next.next
        temp2 = temp2.next
        if temp1 == temp2:
            return 1
    return 0


def MergeNode(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        if temp1.next is None:
            temp1 = head2
        else:
            temp1 = temp1.next
        if temp2.next is None:
            temp2 = head1
        else:
            temp2 = temp2.next
    return temp1.data


def length(head):
    temp = head
    cont = 0
    while temp:
        cont += 1
        temp = temp.next
    return cont


def MergeNode2(head1, head2):
    len1 = length(head1)
    len2 = length(head2)
    n = len2-len1
    bigger = head2
    smaller = head1
    if len1 > len2:
        n = len1-len2
        bigger = head1
        smaller = head2

    for i in range(n):
        bigger = bigger.next

    while bigger and smaller:
        if bigger == smaller:
            return bigger.data
        bigger = bigger.next
        smaller = smaller.next
    return None


l1 = LinkedList()
l1.addNode(5)
l1.addNode(4)
l1.addNode(3)
l1.addNode(2)
l1.addNode(1)
l1.printList()
print('---------')
print(getNodeValueFromTail(l1.head,3))