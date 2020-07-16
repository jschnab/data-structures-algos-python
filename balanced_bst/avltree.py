"""
AVL tree: Adelson-Velskii and Landis invented balanced tree in 1962

Stays balanced -> maintain O(logn) for insert, delete and lookup

Can build tree in O(nlogn), traverse tree in O(n)

path stack: contains nodes along path to the new node's destination (call stack
if using recursion)

pivot: when popping nodes from the path stack, first node with balance
       not equal to 0, i.e. closest ancestor to inserted node with balance
       not equal to 0

bad child: child of the pivot node in the direction of the imbalance
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __iter__(self):
        if self.left is not None:
            for node in self.left:
                yield node
        yield self.val
        if self.right is not None:
            for node in self.right:
                yield node

    def __repr__(self):
        return (
            f"Node({repr(self.val)}, height={repr(self.height)}, "
            f"left={repr(self.left)}, right={repr(self.right)})"
        )


class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def _get_height(self, root):
        if root is None:
            return 0
        return root.height

    def _update_height(self, root):
        height = 1 + max(
            self._get_height(root.left),
            self._get_height(root.right),
        )
        return height

    def _get_balance(self, root):
        return self._get_height(root.right) - self._get_height(root.left)

    def insert(self, val):
        def __insert(root, val):
            if root is None:
                return Node(val)

            if val < root.val:
                root.left = __insert(root.left, val)

            else:
                root.right = __insert(root.right, val)

            root.height = self._update_height(root)
            balance = self._get_balance(root)

            # node added to subtree of bad child
            # in the direction of the imbalance
            if balance < -1 and val < root.left.val:
                return self._right_rotate(root)

            if balance > 1 and val > root.right.val:
                return self._left_rotate(root)

            # node added to subtree of bad child
            # in the direction opposite to the imbalance
            if balance < -1 and val > root.left.val:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

            if balance > 1 and val < root.right.val:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

            return root

        self.root = __insert(self.root, val)

    def _left_rotate(self, root):
        a = root.right
        b = a.left

        # perform rotation
        a.left = root
        root.right = b

        # update heights
        root.height = self._update_height(root)
        a.height = self._update_height(a)

        return a

    def _right_rotate(self, root):
        a = root.left
        b = a.right

        # perform rotation
        a.right = root
        root.left = b

        # update weights
        root.height = self._update_height(root)
        a.height = self._update_height(a)

        return a

    def __iter__(self):
        return iter(self.root)

    def __repr__(self):
        return f"AVLTree({repr(self.root)})"
