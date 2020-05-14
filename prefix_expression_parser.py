from queue import Queue

from ast import NumNode, PlusNode, TimesNode


def E(q):
    if q.empty():
        raise ValueError("invalid prefix expression")

    token = q.get()
    print(q.qsize())

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
    root = E(q)
    print(root.eval())
    print(root.inorder())


if __name__ == "__main__":
    main()
