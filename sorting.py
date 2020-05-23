import random


def select(seq, start):
    min_idx = start
    for j in range(start + 1, len(seq)):
        if seq[j] < seq[min_idx]:
            min_idx = j
    return min_idx


def selection_sort(seq):
    for i in range(len(seq) - 1):
        min_idx = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[min_idx]
        seq[min_idx] = tmp


def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    # merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1

    # copy in the rest of the start-to-mid sequence
    while i < mid:
        lst.append(seq[i])
        i += 1

    # no need to copy the rest of the sequence from j to stop
    # the next part of the code does this for us
    # so no need to do:
    # while j < stop:
    #     lst.append(seq[j])
    #     j += 1

    # copy elements back to the original sequence
    for i in range(len(lst)):
        seq[start + i] = lst[i]


def merge_sort_recursive(seq, start, stop):
    #  >= is necessary if sequence is empty
    # otherwise start == stop - 1 does the job
    if start >= stop - 1:
        return

    mid = (start + stop) // 2

    merge_sort_recursive(seq, start, mid)
    merge_sort_recursive(seq, mid, stop)
    merge(seq, start, mid, stop)


def merge_sort(seq):
    merge_sort_recursive(seq, 0, len(seq))


if __name__ == "__main__":
    seq = [random.randint(0, 100) for _ in range(10)]
    print("Before sort:", seq)
    merge_sort(seq)
    print("After sort:", seq)
