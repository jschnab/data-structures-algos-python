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
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

    # methods of the BinarySearchTree class
    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            """
            Recursive function, static function (not method of the class)
            hidden inside the insert function.
            """
            if root == None:
                return BinarySearchTree.__Node(val)

            if val < root.get_val():
                root.set_left(__insert(root.get_left(), val))

            if val > root.get_val():
                root.set_right(__insert(root.get_right(), val))

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)


if __name__ == "__main__":
    main()
