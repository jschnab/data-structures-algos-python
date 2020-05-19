from queue import Queue

from ast import NumNode, PlusNode, TimesNode


def E(q):
    if q.empty():
        raise ValueError("invalid prefix expression")

    token = q.get()

    if token == "+":
        return PlusNode(E(q), E(q))

    if token == "*":
        return TimesNode(E(q), E(q))

    return NumNode(float(token))


def main():
    x = input("Please enter a prefix expression: ")
    lst = x.split()
    q = Queue()
    for token in lst:
        q.put(token)
    try:
        root = E(q)
        print("Infix form: ", root.inorder())
        print("Postfix form: ", root.postorder())
        print("Result: ", root.eval())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
