class Heap:
    def __init__(self, sequence=None):
        if sequence is not None:
            self.build_from(sequence)

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

    def sort_items(self):
        for last in range(self.size - 1, 0, -1):
            print(
                f"swapping items[0] = {self.items[0]} and items[{last}] "
                f"= {self.items[last]}"
            )
            tmp = self.items[0]
            self.items[0] = self.items[last]
            self.items[last] = tmp
            print(f"swapping result: {self.items}")
            print(f"sifting {self.items[0]} from 0 to {last}")
            self._sift_down_from_to(0, last)
            print(f"sifting result: {self.items}")

    def _swap_parent_child(self, parent_idx, child_side):
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

    def _sift_down_from_to(self, from_, last_):
        """
        from_ is the index of an element in the heap.

        Before: items[from_..last_] satisfies the heap condition, except
        perhaps for the element items[from_]

        After: items[from_] is sifted down as far as necessary to maintain the
        heap structure for items[from_..last_]
        """
        # sift the item down to maintain the heap structure
        while True:

            parent = self.items[from_]
            left = self._left_child(from_)
            right = self._right_child(from_)

            # parent has both children
            if left and right:
                if left > right:
                    # if parent < left child, swap them
                    if parent < left and self._left_child_idx(from_) < last_:
                        from_ = self._swap_parent_child(from_, "left")
                    # else the heap structure is maintained and we stop
                    else:
                        break

                else:
                    # if parent < right child, swap them
                    if parent < right and self._right_child_idx(from_) < last_:
                        from_ = self._swap_parent_child(from_, "right")
                    # else the heap structure is maintained and we stop
                    else:
                        break

            # parent has only left child
            elif left:
                if parent < left and self._left_child_idx(from_) < last_:
                    from_ = self._swap_parent_child(from_, "left")
                else:
                    break

            # parent has only right child
            elif right:
                if parent < left and self._left_child_idx(from_) < last_:
                    from_ = self._swap_parent_child(from_, "left")
                else:
                    break

            # parent has no children
            else:
                break


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


if __name__ == "__main__":
    test6()
