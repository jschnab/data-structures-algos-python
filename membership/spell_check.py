import string

from bloom import BloomFilter
from trie import Trie


def read_file(file_name):
    """
    Get the list of words from a text file.

    :param str file_name: name of the file to read
    :return list[str]: list of words
    """
    words = []
    with open(file_name) as f:
        for line in f:
            for word in line.strip().split():
                words.append(word.strip(string.punctuation).lower())
    return words


def get_dictionary_trie(file_name):
    """
    Get a dictionary as a trie data-structure from a text file.

    :param str file_name: name of the file storing the dictionary
    :return Trie: dictionary
    """
    trie = Trie()
    with open(file_name) as f:
        for line in f:
            trie.insert(line.strip())
    return trie


def get_dictionary_bloom(file_name):
    """
    Get a dictionary as a Bloom filer data-structure from a text file.

    :param str file_name: name of the file storing the dictionary
    :return BloomFilter: dictionary
    """
    bloom = BloomFilter()
    with open(file_name) as f:
        for line in f:
            bloom.insert(line.strip())
    return bloom


def spell_check(to_check, dictionary):
    """
    Spell check a text given a dictionary.

    :param str to_check: text file storing the text to check
    :param str dictionary: text file storing the dictionary
    """
    print("reading file to check")
    words = read_file(to_check)
    print("generating dictionary")
    dic = get_dictionary_trie(dictionary)
    print("check spelling for the following words:")
    for w in words:
        if w not in dic:
            print(f"    {w}")


if __name__ == "__main__":
    spell_check(
        "/home/jonathans/Downloads/independence.txt",
        "/home/jonathans/Downloads/wordsEn.txt"
    )
