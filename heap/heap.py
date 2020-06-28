from random import randint


class Heap:
    def __init__(self, sequence=None, verbose=False):
        if sequence is not None:
            self.build_from2(sequence, verbose)

    def __str__(self):
        return f"largest-on-top heap: {self.items}"

    def __repr__(self):
        return str(self)

    def build_from(self, sequence, verbose=False):
        """
        The items are copied into the heap and ordered.
        This method works in a top-down fashion: we find the item which
        should be at the top of the heap and build the heap going down.
        Time complexity: O(nlogn)

        :param iterable sequence: collection of items which understands
                                  the comparison operators
        :param bool verbose: if True, print debugging information
        """
        self.items = list(sequence)
        self.size = len(self.items)
        if verbose:
            print(f"items: ", self.items)
        for i in range(1, self.size):
            self._sift_up_from(i)
        if verbose:
            print("heap: ", self.items)

    def build_from2(self, sequence, verbose=False):
        """
        The items are copied into the heap and ordered.
        This is method is an improvement of build_from() and works in a
        bottom-up fashion: since the heap is a binary heap half the nodes
        are parents and half the nodes are leaves, so we start from the
        middle of the array of items and sift them down to their position.
        Then, we move up in the tree (lower indices) and repeat.
        Time complexity: O(n)

        :param iterable sequence: collection of items which understands
                                  the comparison operators
        :param bool verbose: if True, print debugging information
        """

        self.items = list(sequence)
        self.size = len(self.items)
        start = (self.size - 2) // 2
        if verbose:
            print(f"items: ", self.items)
            print(f"start index: {start}")
        for i in range(start, -1, -1):
            if verbose:
                print(f"sifting down item[{i}] = {self.items[i]}")
            self._sift_down_from_to(i, self.size)
            if verbose:
                print(f"sifting result: ", self.items)
        if verbose:
            print("heap: ", self.items)

    def _parent_idx(self, idx):
        return (idx - 1) // 2

    def _left_child_idx(self, idx):
        return 2 * idx + 1

    def _right_child_idx(self, idx):
        return 2 * idx + 2

    def _left_child(self, parent_idx):
        try:
            return self.items[self._left_child_idx(parent_idx)]
        except IndexError:
            return None

    def _right_child(self, parent_idx):
        try:
            return self.items[self._right_child_idx(parent_idx)]
        except IndexError:
            return None

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

    def sort_items(self, verbose=False):
        """
        Starting from a heap, sort the heap items in ascending order,
        in place.

        :param bool verbose: if True, print debugging messages
        """
        for last in range(self.size - 1, 0, -1):
            if verbose:
                print(
                    f"swapping items[0] = {self.items[0]} and items[{last}] "
                    f"= {self.items[last]}"
                )
            tmp = self.items[0]
            self.items[0] = self.items[last]
            self.items[last] = tmp
            if verbose:
                print(f"swapping result: {self.items}")
                print(f"sifting {self.items[0]} from 0 to {last}")
            self._sift_down_from_to(0, last)
            if verbose:
                print(f"sifting result: {self.items}")

    def _swap_parent_child(self, parent_idx, child_side):
        """
        Swap a parent with one of its child and return the child index.

        :param int parent_idx: index of the parent
        :param str child_side: side of the child to consider swapping with
                               ('left' or 'right')
        :return int: index of the child the parent was swapped with
        """
        if child_side == "left":
            tmp = self.items[parent_idx]
            self.items[parent_idx] = self._left_child(parent_idx)
            self.items[self._left_child_idx(parent_idx)] = tmp
            return self._left_child_idx(parent_idx)

        elif child_side == "right":
            tmp = self.items[parent_idx]
            self.items[parent_idx] = self._right_child(parent_idx)
            self.items[self._right_child_idx(parent_idx)] = tmp
            return self._right_child_idx(parent_idx)

    def _sift_down_from_to(self, start, end, verbose=False):
        """
        'start' is the index of an element in the heap.

        Before: items[start..end] satisfies the heap condition, except
        perhaps for the element items[start]

        After: items[start] is sifted down as far as necessary to maintain the
        heap structure for items[start..end]
        """
        # sift the item down to maintain the heap structure
        while True:

            parent = self.items[start]
            if self._left_child_idx(start) >= end:
                left = None
            else:
                left = self._left_child(start)
            if self._right_child_idx(start) >= end:
                right = None
            else:
                right = self._right_child(start)

            # parent has both children
            if left is not None and right is not None:
                if left > right:
                    # if parent < left child, swap them
                    if parent < left:
                        start = self._swap_parent_child(start, "left")
                    # else the heap structure is maintained and we stop
                    else:
                        break

                else:
                    # if parent < right child, swap them
                    if parent < right:
                        start = self._swap_parent_child(start, "right")
                    # else the heap structure is maintained and we stop
                    else:
                        break

            # parent has only left child
            elif left is not None and parent < left:
                start = self._swap_parent_child(start, "left")

            # we dont check if parent has only right child
            # because we sort the items from highest (right-most) to
            # lowest (left-most)

            # parent has no children
            else:
                break


def heapsort(sequence):
    """
    Sort an iterable using a heap.

    :param iterable sequence: sequence of items to be sorted
    :param bool verbose: if True, print debugging information
    :return list: sorted sequence
    """
    h = Heap(sequence)
    h.sort_items()
    return h.items


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
    h.items = [57, 71, 36, 15, 101]
    h._sift_down_from_to(0, 4)
    print(h.items)


def test5():
    h = Heap([71, 15, 36, 57, 101])
    h.sort_items()
    print(h.items)


def test6():
    h = Heap([10, 30, -100, 50, 20, 30, -40, 70, 5, 50])
    h.sort_items()
    print(h.items)


def test7():
    h = Heap([15, -34, 23, 46, 24, 20], verbose=True)
    print(h.items)


def test8():
    seq = [randint(-100, 100) for _ in range(10)]
    h = Heap(seq, True)
    print(h.items)


def test9():
    seq = [randint(-100, 100) for _ in range(5)]
    print(heapsort(seq, verbose=True))


def test10():
    seq = (806, 1, 33, 9, 0, -87)
    print(heapsort(seq, verbose=True))


if __name__ == "__main__":
    test9()
