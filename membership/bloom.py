SIZE = 1000 * 1000
N_HASH = 7


class BloomFilter:
    def __init__(self, size=SIZE, n_hash=N_HASH):
        self.array = [0] * SIZE

    def insert(self, item):
        for i in range(N_HASH):
            self.array[hash(item + str(i)) % SIZE] = 1

    def __contains__(self, item):
        for i in range(N_HASH):
            if self.array[hash(item + str(i)) % SIZE] != 1:
                return False
        return True
