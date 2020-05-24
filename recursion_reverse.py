import random

from string import ascii_letters
from timing import timing

import matplotlib.pyplot as plt


def reverse_list(l):
    accumulator = []
    for i in l:
        accumulator = [i] + accumulator
    return accumulator


def reverse_list_recur(lst):
    if lst == []:
        return []
    tail = reverse_list_recur(lst[1:])
    head = lst[:1]
    return tail + head


def reverse_str_recur(s):
    if s == "":
        return ""
    tail = reverse_str_recur(s[1:])
    head = s[:1]
    return tail + head


def reverse_list_index(l):
    def helper(i):
        if i == -1:
            return []
        tail = helper(i - 1)
        head = [l[i]]
        return head + tail

    return helper(len(l) - 1)


def reverse(seq):
    seq_type = type(seq)
    empty = seq_type()
    if seq == empty:
        return empty
    tail = reverse(seq[1:])
    head = seq[:1]
    return tail + head


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def len_str(s):
    if s == "":
        return 0
    return 1 + len_str(s[1:])


def swap(s):
    if len_str(s) < 2:
        return s
    if len_str(s) == 2:
        return s[1] + s[0]
    return swap(s[:2]) + swap(s[2:])


def random_strings(length, n):
    result = []
    for _ in range(n):
        result.append(
            "".join(random.choice(ascii_letters) for _ in range(length))
        )
    return result


def make_test_strings(mini, maxi, n):
    tests = []
    for i in range(mini, maxi + 1):
        tests.append(random_strings(i, n))
    return tests


if __name__ == "__main__":
    mini = 1
    maxi = 20
    rep = 10
    tests = make_test_strings(mini, maxi, rep)
    times = []
    for t in tests:
        times.append(timing(reverse, t) / rep)
    fig, ax = plt.subplots()
    ax.plot(list(range(mini, maxi + 1)), times)
    ax.set_xlabel("Sequence size", fontsize=14)
    ax.set_ylabel("Time (ms)", fontsize=14)
    ax.grid(linestyle=":")
    plt.show()
