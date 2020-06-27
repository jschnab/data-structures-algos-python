class Heap:
    def __init__(self):
        self.items = []

    def build_from(self, sequence):
        """
        The items are copied into the heap and ordered.

        :param iterable sequence: collection of items which understands
                                  the comparison operators
        """
        self.items = list(sequence)
        self.size = len(self.items)
        for i in range(1, self.size):
            self._sift_up_from(i)

    def _parent_idx(self, idx):
        return (idx - 1) // 2

    def _left_child_idx(self, idx):
        return 2 * idx + 1

    def _right_child_idx(self, idx):
        return 2 * idx + 2

    def _sift_up_from(self, child_idx):
        """
        Sifts the child node up as far as necessary to ensure the path to
        the root of the heap satisfies the heap condition.

        :param int child_idx: index of a node in the heap
        """
        while self.items[child_idx] > self.items[self._parent_idx(child_idx)]:
            if child_idx == 0:
                break
            tmp = self.items[child_idx]
            self.items[child_idx] = self.items[self._parent_idx(child_idx)]
            self.items[self._parent_idx(child_idx)] = tmp
            child_idx = self._parent_idx(child_idx)

    def add_to_heap(self, item):
        """
        Add the item to the heap, maintaining it as a heap of the same type.

        :param int item: item to add to the heap
        """
        self.items.append(item)
        self._sift_up_from(self.size)
        self.size += 1


def test1():
    h = Heap()
    h.build_from([71, 15, 36, 57, 101])
    print(h.items)


def test2():
    h = Heap()
    h.build_from([110, 58, 85, 34, 17, 27, 78, 12, 98])
    h._sift_up_from(8)
    print(h.items)


def test3():
    h = Heap()
    h.build_from([110, 58, 85, 34, 17, 27, 78, 12])
    h.add_to_heap(98)
    print(h.items)


def test4():
    h = Heap()
    h.build_from([71, 15, 36, 57, 101])
    h.get_items()
    print(h.items)


if __name__ == "__main__":
    test4()
