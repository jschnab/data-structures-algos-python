class BinarySearchTree:
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

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

        # inorder traversal of the tree (get values in ascending order)
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

        def __eq__(self, other):
            if self.val == other:
                return True
            return False

        def get_rightmost(self):
            if self.right is not None:
                return self.right.get_rightmost()
            return self.val

        def lookup(self, value):
            if value == self.val:
                return True
            if value > self.val and self.right:
                return self.right.lookup(value)
            if value < self.val and self.left:
                return self.left.lookup(value)
            return False

    # methods of the BinarySearchTree class
    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            """
            Recursive function, static function (not method of the class)
            hidden inside the insert function.
            """
            if root is None:
                return BinarySearchTree.__Node(val)

            if val < root.get_val():
                root.set_left(__insert(root.get_left(), val))

            if val > root.get_val():
                root.set_right(__insert(root.get_right(), val))

            return root

        self.root = __insert(self.root, val)

    def get_rightmost(self):
        if self.root is not None:
            return self.root.get_rightmost()

    def delete(self, val):
        def __delete(root, val):
            if root is None:
                return

            if root.get_val() == val and not root.get_left() \
                    and not root.get_right():
                return

            if root.get_val() == val and root.get_left() \
                    and not root.get_right():
                return root.get_left()

            if root.get_val() == val and not root.get_left() \
                    and root.get_right():
                return root.get_right()

            if root.get_val() == val and root.get_left() \
                    and root.get_right():
                rightmost = root.get_left().get_rightmost()
                root.set_val(rightmost)
                root.set_left(__delete(root.get_left(), rightmost))

            if val < root.get_val():
                root.set_left(__delete(root.get_left(), val))

            if val > root.get_val():
                root.set_right(__delete(root.get_right(), val))

            return root

        self.root = __delete(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def contains(self, value):
        if self.root is not None:
            return self.root.lookup(value)
        return False


def main():
    print("Binary Search Tree Program")
    print("--------------------------")
    print("1. Insert\n2. Delete\n3. Lookup\n")

    tree = BinarySearchTree()

    while True:

        choice = input("Choice?")
        if not choice:
            print("Exiting")
            break

        if choice == "1":
            while True:
                insert = input("Insert?")
                if not insert:
                    break
                tree.insert(float(insert))

        elif choice == "2":
            while True:
                delete = input("Delete?")
                if not delete:
                    break
                tree.delete(float(delete))

        elif choice == "3":
            while True:
                value = input("Value?")
                if not value:
                    break
                if tree.contains(float(value)):
                    print(f"Yes, {value} is in the tree")
                else:
                    print(f"No, {value} is not in the tree")


if __name__ == "__main__":
    main()
