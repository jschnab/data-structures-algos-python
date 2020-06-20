class Trie:
    class TrieNode:
        def __init__(self, item, next_=None, follows=None):
            self.item = item
            self.next = next_
            self.follows = follows

    def __init__(self):
        self.start = None

    def __insert(self, node, item):
        if not item:
            return

        if node is None:
            return Trie.TrieNode(
                item[0],
                follows=self.__insert(None, item[1:])
            )

        if item[0] == node.item:
            node.follows = self.__insert(node.follows, item[1:])
            return node

        node.next = self.__insert(node.next, item)
        return node

    def insert(self, item):
        self.start = self.__insert(self.start, item + "$")

    def __contains(self, node, item):
        if len(item) == 0:
            return True

        if node is None:
            return False

        if item[0] == node.item:
            return self.__contains(node.follows, item[1:])

        return self.__contains(node.next, item)

    def __contains__(self, item):
        return self.__contains(self.start, item + "$")
