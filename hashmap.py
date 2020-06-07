from hashset import HashSet


class HashMap:
    class __KVPair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.key == other.key

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def __hash__(self):
            return hash(self.key)

    def __init__(self):
        self.hash_set = HashSet()

    def __len__(self):
        return len(self.hash_set)

    def __contains__(self, item):
        return HashMap.__KVPair(item, None) in self.hash_set

    def not__contains__(self, item):
        return item not in self.hash_set

    def __setitem__(self, key, value):
        self.hash_set.add(HashMap.__KVPair(key, value))

    def __getitem__(self, key):
        if HashMap.__KVPair(key, None) in self.hash_set:
            return self.hash_set[HashMap.__KVPair(key, None)].get_value()
        raise KeyError(f"Key '{key}' not in HashMap")

    def __iter__(self):
        for i in self.hash_set:
            yield i.get_key()

    def __str__(self):
        s = "{"
        items = []
        for i in self.hash_set:
            items.append(f"{repr(i.get_key())}: {repr(i.get_value())}")
        s += ", ".join(items)
        s += "}"
        return s

    def __repr__(self):
        return str(self)
