class HashSet:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.num_items = 0
        for item in contents:
            self.add(item)

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] is not None:
            if items[idx] == item:
                return False

            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True

    def __rehash(old_list, new_list):
        for x in old_list:
            if x is not None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, new_list)
        return new_list

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.num_items += 1
            load = self.num_items / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(
                    self.items,
                    [None] * 2 * len(self.items),
                )

    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] is not None:
            if items[idx] == item:
                next_idx = (idx + 1) % len(items)
                if items[next_idx] is None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.num_items -= 1
            load = max(self.num_items, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(
                    self.items, [None] * int(len(self.items) / 2)
                )
        else:
            raise KeyError("Item not in HashSet")

    def discard(self, item):
        if HashSet.__remove(item, self.items):
            self.num_items -= 1
            load = max(self.num_items, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(
                    self.items, [None] * int(len(self.items) / 2)
                )

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return True
            idx = (idx + 1) % len(self.items)
        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] is not None \
                    and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

    def __len__(self):
        return self.num_items

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return self.items[idx]
            idx = (idx + 1) % len(self.items)

    def is_disjoint(self, other):
        if (len(self) == 0) or (len(other) == 0):
            return True
        if len(self) < len(other):
            self, other = other, self
        for i in other:
            if i in self:
                return False
        return True

    def is_subset(self, other):
        return all(i in other for i in self)

    def is_superset(self, other):
        return other.is_subset(self)

    def union(self, other):
        result = HashSet()
        for i in self:
            result.add(i)
        for i in other:
            result.add(i)
        return result

    def intersection(self, other):
        result = HashSet()
        if len(self) < len(other):
            self, other = other, self
        for i in self:
            if i in other:
                result.add(i)
        return result

    def difference_update(self, other):
        for i in other:
            self.discard(i)

    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result

    def symmetric_difference(self, other):
        return self.difference(other).union(other.difference(self))

    def copy(self):
        other = HashSet()
        for i in self:
            other.add(i)
        return other

    def __str__(self):
        s = "{"
        s += ", ".join(repr(i) for i in self)
        s += "}"
        return s

    def __repr__(self):
        return str(self)
