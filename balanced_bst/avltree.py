class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


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

            if balance > 1 and val < root.left.val:
                return self._right_rotate(root)

            if balance < -1 and val > root.right.val:
                return self._left_rotate(root)

            if balance > 1 and val > root.left.val:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

            if balance < -1 and val < root.right.val:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        self.root = __insert(self.root, val)

    def _left_rotate(self, root):
        a = root.right
        b = a.left

        # perform rotation
        a.left = root
        root.left = b

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
