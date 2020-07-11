"""
Definitions

path stack: contains nodes along path to the new node's destination

pivot: when popping nodes from the path stack, first node with balance
       not equal to 0, i.e. closest ancestor to inserted node with balance
       not equal to 0

bad child: child of the pivot node in the direction of the imbalance
"""

class AVLTree:
    class AVLNode:
        def __init__(
            self,
            val,
            balance=0,
            left=None,
            right=None,
        ):
            self.val = val
            self.left = left
            self.right = right
            self.balance = balance
            self.height = 1

        def get_val(self):
            return self.val

        def set_val(self, newval):
            self.val = newval

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def set_left(self, newleft):
            self.left = newleft

        def set_right(self, newright):
            self.right = newright

        def get_height(self):
            return self.height

        # inorder traversal of the tree (get values in ascending order)
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            rep = (
                f"AVLTree.AVLNode({repr(self.val)}, balance="
                f"{repr(self.balance)}, height={repr(self.height)}, "
                f"left={repr(self.left)}, right={repr(self.right)})"
            )
            return rep

    def __init__(self, root=None):
        self.root = root

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        left_height = self._get_height(root.get_left())
        right_height = self._get_height(root.get_right())
        return right_height - left_height

    def insert(self, val):

        def __insert(root, val):
            if root is None:
                return AVLTree.AVLNode(val)

            if val < root.get_val():
                root.set_left(__insert(root.get_left(), val))

            else:
                root.set_right(__insert(root.get_right(), val))

            root.height = max(
                self._get_height(root.get_left()),
                self._get_height(root.get_right()),
            ) + 1

            root.balance = self._get_balance(root)

            if root.balance < -1:
                child = root.left
                if child is None:
                    return
                root.set_left(child.get_right())
                child.set_right(root)
                return child

            return root

        self.found_pivot = False
        self.root = __insert(self.root, val)

    def __repr__(self):
        return f"AVLTree({repr(self.root)})"

    def __iter__(self):
        return iter(self.root)
