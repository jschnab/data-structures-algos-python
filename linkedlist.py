class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self, item):
        self.item = item

    def set_next(self, nxt):
        self.next = nxt


class LinkedList:
    class __Node:
        def __init__(self, item, nxt=None):
            self.item = item
            self.next = nxt

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_item(self, item):
            self.item = item

        def set_next(self, nxt):
            self.next = nxt

    def __init__(self, contents=[]):
        """
        Keep a reference to the first node and last node of the list.
        Both point to a dummy node to begin with.
        The purpose of dummy nodes is to eliminate special cases.
        """
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.num_items = 0
        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()
            return cursor.get_item()
        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()
            cursor.set_item(val)
            return
        raise IndexError("LinkedList index out of range")

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                f"Concatenate undefined for {str(type(self))} + "
                f"{str(type(other))}"
            )

        result = LinkedList()
        cursor = self.first.get_next()
        while cursor is not None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        cursor = other.first.get_next()
        while cursor is not None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        return result

    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.set_next(node)
        self.last = node
        self.num_items += 1

    def insert(self, index, item):
        cursor = self.first
        if index < self.num_items:
            for i in range(index):
                cursor = cursor.get_next()
            node = LinkedList.__Node(item, cursor.get_next())
            cursor.set_next(node)
            self.num_items += 1
        else:
            self.append(item)

    def __delitem__(self, index):
        if index >= 0 and index < self.num_items:
            cursor = self.first
            for i in range(index):
                cursor = cursor.get_next()
            cursor.set_next(cursor.get_next().get_next())
            if index == self.num_items - 1:
                self.last = cursor
            self.num_items -= 1
            return
        raise IndexError("LinkedList index out of range")

    def __iter__(self):
        cursor = self.first.get_next()
        for _ in range(self.num_items):
            yield cursor.get_item()
            cursor = cursor.get_next()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.num_items != other.num_items:
            return False
        cur_self = self.first.get_next()
        cur_other = other.first.get_next()
        for _ in range(self.num_items):
            if cur_self.get_item() != cur_other.get_item():
                return False
            cur_self = cur_self.get_next()
            cur_other = cur_other.get_next()
        return True

    def __len__(self):
        return self.num_items
