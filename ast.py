class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " *"


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"

    def postorder(self):
        return self.left.postorder() + " " + self.right.postorder() + " +"


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

    def postorder(self):
        return str(self.num)


def main():
    a = NumNode(5)
    b = NumNode(4)
    c = NumNode(3)
    d = NumNode(2)
    t1 = TimesNode(a, b)
    t2 = TimesNode(c, d)
    root = PlusNode(t1, t2)
    print(root.postorder())
    print(root.eval())


if __name__ == "__main__":
    main()
