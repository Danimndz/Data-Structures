# izq menor
# derecha mayor
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self, searchData):
        if self.data == searchData:
            return True
        elif searchData < self.data:
            if self.left:
                return self.left.search(searchData)
            else:
                return False
        else:
            if self.right:
                return self.right.search(searchData)
            else:
                return False

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data)
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data)

    def preOrder(self):
        print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, " ")
        if self.right:
            self.right.printTree()


def inOrderIterative(root: Node) -> None:
    # left root right
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break


def preOrderIterative(root: Node) -> None:
    # root left right
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            print(current.data)
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break


def findInOrderSuccessor(root: Node, node: Node,) -> object:
    # case 1: the tree has right subtree.
    # Go to the right left-more subtree.
    if node.right != None:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp.data
    # case 2: the tree doesn't have right subtree:
    # find the left most antecesor
    elif node.right is None:
        antecesorParent = Node(None)
        while node.data != root.data:
            # if the value is in the right just move..
            if node.data > root.data:
                root = root.right
            elif node.data < root.data:
                antecesorParent = root
                root = root.left
        return antecesorParent.data


def maxDepth(node):
    if node is None:
        return 0
    else:
        depthR = maxDepth(node.right)
        depthL = maxDepth(node.left)
    maximum = depthR if depthR > depthL else depthL
    return maximum+1    



def traverseTree(root: Node, low: int, high: int, suma) -> int:
    if root is None:
        return
    if low <= root.data <= high:
        suma += root.data
    if root.right:
        suma = traverseTree(root.right, low, high, suma)
    elif root.left:
        suma = traverseTree(root.left, high, low, suma)
    return suma


def sumNode(root: Node, low: int, high: int) -> int:
    return traverseTree(root, low, high, 0)


def sumNodeIterative(root: Node, low: int, high: int) -> int:
    suma = 0
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            if low <= current.val <= high:
                suma += current.val
            current = current.right
        else:
            break
    return suma


def lca(root: Node, v1: int, v2: int) -> Node:
    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    elif root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    return root
        # root = Node(1)
        # root.left = Node(2)
        # root.right = Node(3)
        # root.left.left = Node(4)
        # root.left.right = Node(5)

        # print(maxDepth(root))

root = Node(2)
root.insert(1)
root.insert(4)
root.insert(3)
root.insert(5)
root.insert(6)
# root.printTree()

res = lca(root,3,6)
print(res.data)

# root.printTree()
# print("inOrder")
# L,ROOT,R
# print('recursivo:')
# root.inOrder()
# print('iterativo:')
# inOrderIterative(root)
# ROOT,L,R
# print('recursivo:')
# root.preOrder()
# print('iterativo:')
# preOrderIterative(root)
# L,R,ROOT
# root.postOrder()

# succesor = root.left.right.left
# print("sucesor de:", succesor.data)
# print(root.findInOrderSuccessor(root, succesor))
