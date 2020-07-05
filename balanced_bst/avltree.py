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
            item,
            balance=0,
            left=None,
            right=None,
        ):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def __repr__(self):
            rep = (
                f"AVLTree.AVLNode({repr(self.item)}, balance="
                f"{repr(self.balance)}, left={repr(self.left)}, "
                f"right={repr(self.right)}"
            )
            return rep
