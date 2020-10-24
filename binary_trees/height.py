from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    """
    Get tree height using breadth-first search.

    :param TreeNode root: root of the tree
    :returns (int): height of the tree
    """
    if not root:
        return 0
    q = deque([root])
    height = 0
    while True:
        count = len(q)
        if count == 0:
            break
        while count > 0:
            node = q.pop()
            count -= 1
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        height += 1
    return height


def test1():
    root = None
    assert height(root) == 0
    print("test 1 successful")


def test2():
    root = TreeNode(3)
    assert height(root) == 1
    print("test 2 successful")


def test3():
    root = TreeNode(3, TreeNode(4), TreeNode(5))
    assert height(root) == 2
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
