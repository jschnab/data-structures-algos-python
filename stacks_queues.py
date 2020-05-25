from linkedlist import LinkedList


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Attempt to pop an empty stack")
        top_idx = len(self.items) - 1
        item = self.items[top_idx]
        del self.items[top_idx]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.is_empty():
            raise RuntimeError("Attempt to get top of empty stack")
        top_idx = len(self.items) - 1
        return self.items[top_idx]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        item = self.items[0]
        del self.items[0]
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.is_empty():
            raise RuntimeError("Attempt to access front of empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def test_stack():
    s = Stack()

    lst1 = list(range(10))
    for i in lst1:
        s.push(i)
    if s.top() == 9:
        print("test 1 passed")
    else:
        print("test 1 failed")

    lst2 = []
    while not s.is_empty():
        lst2.append(s.pop())
    lst2.reverse()
    if lst1 != lst2:
        print("test 2 failed")
    else:
        print("test 2 passed")

    try:
        s.pop()
        print("test 3 failed")
    except RuntimeError:
        print("test 3 passed")

    try:
        s.top()
        print("test4 failed")
    except RuntimeError:
        print("test 4 passed")


def test_queue():
    q = Queue()

    lst1 = list(range(10))
    for i in lst1:
        q.enqueue(i)
    if q.front() == 0:
        print("test 1 passed")
    else:
        print("test 1 failed")

    lst2 = []
    while not q.is_empty():
        lst2.append(q.dequeue())
    if lst1 != lst2:
        print("test 2 failed")
    else:
        print("test 2 passed")

    try:
        q.dequeue()
        print("test 3 failed")
    except RuntimeError:
        print("test 3 passed")

    try:
        q.front()
        print("test4 failed")
    except RuntimeError:
        print("test 4 passed")


if __name__ == "__main__":
    test_queue()
