class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def inorder_iterative(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right


def inorder_recursive(node):
    if node.left:
        inorder_recursive(node.left)
    print(node.val)
    if node.right:
        inorder_recursive(node.right)


def preorder_iterative(node):
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        print(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def preorder_recursive(node):
    print(node.val)
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
        print(output.pop().val)


def postorder_recursive(node):
    if node.left:
        postorder_recursive(node.left)
    if node.right:
        postorder_recursive(node.right)
    print(node.val)


def morris(node):
    """
    Perform inorder tree traversal using the Morris algorithm.

    Time complexity: O(n)
    Space complexity: O(1) since we don't store a stack or queue of nodes
    """
    result = []
    while node:
        if node.left:
            predecessor = node.left
            while predecessor.right and predecessor.right != node:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = node
                node = node.left
            else:
                result.append(node.val)
                predecessor.right = None
                node = node.right
        else:
            result.append(node.val)
            node = node.right

    return result


def test1():
    root = Node("+")
    root.left = Node("*")
    root.right = Node(3)
    root.left.left = Node("+")
    root.left.right = Node(6)
    root.left.left = Node("+")
    root.left.left.left = Node(5)
    root.left.left.right = Node(4)
    preorder_iterative(root)


def test2():
    t = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    assert morris(t) == [1, 2, 3, 4, 5, 6, 7]
    print("test 2 successful")


def test3():
    t = Node(4, None, Node(5, None, Node(6, None, Node(7))))
    assert morris(t) == [4, 5, 6, 7]
    print("test 3 successful")


def test4():
    t = Node(4, Node(3, Node(2, Node(1))))
    assert morris(t) == [1, 2, 3, 4]
    print("test 4 successful")


def test5():
    t = None
    assert morris(t) == []
    print("test 5 successful")


if __name__ == "__main__":
    test2()
    test3()
    test4()
    test5()
