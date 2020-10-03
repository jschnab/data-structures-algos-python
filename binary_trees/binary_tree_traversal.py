class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_iterative(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.value)
            node = node.right


def inorder_recursive(node):
    if node.left:
        inorder_recursive(node.left)
    print(node.value)
    if node.right:
        inorder_recursive(node.right)


def preorder_iterative(node):
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def preorder_recursive(node):
    print(node.value)
    if node.left:
        preorder_recursive(node.left)
    if node.right:
        preorder_recursive(node.right)


def postorder_iterative(node):
    stack = []
    stack.append(node)
    output = []

    while stack:
        current = stack.pop()
        if current:
            output.append(current)

        # append left first
        # then left is appended last to the output
        # so it will be printed first
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    while output:
        print(output.pop().value)


def postorder_recursive(node):
    if node.left:
        postorder_recursive(node.left)
    if node.right:
        postorder_recursive(node.right)
    print(node.value)


if __name__ == "__main__":
    root = Node("+")
    root.left = Node("*")
    root.right = Node(3)
    root.left.left = Node("+")
    root.left.right = Node(6)
    root.left.left = Node("+")
    root.left.left.left = Node(5)
    root.left.left.right = Node(4)
    preorder_iterative(root)
