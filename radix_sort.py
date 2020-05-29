from stacks_queues import Queue


def char_at(s, i):
    if len(s) - 1 < i:
        return " "
    return s[i]


def radix_sort(words):
    main = Queue()
    queues = [Queue() for _ in range(128)]

    longest = 0
    for w in words:
        length = len(w)
        if length > longest:
            longest = length
        main.enqueue(w)

    i = longest - 1
    while i >= 0:
        while not main.is_empty():
            current = main.dequeue()
            queues[ord(char_at(current, i))].enqueue(current)

        for j in range(128):
            while not queues[j].is_empty():
                current = queues[j].dequeue()
                main.enqueue(current)

        i -= 1

    answer = []
    while not main.is_empty():
        answer.append(main.dequeue())

    return answer


if __name__ == "__main__":
    words = ["cat", "hat", "car", "barn", "farm", "bat"]
    print(radix_sort(words))
