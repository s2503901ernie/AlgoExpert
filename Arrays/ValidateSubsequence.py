"""
Test case

array
[5, 1, 22, 25, 6, -1, 8, 10]
sequence
[1, 6, -1, 10]

"""


def solution_1(array, sequence):
    """
    O(n) time
    O(1) space

    """
    idx_array = 0
    idx_sequence = 0
    while idx_array < len(array) and idx_sequence < len(sequence):
        if array[idx_array] == sequence[idx_sequence]:
            idx_sequence += 1
        idx_array += 1

    return idx_sequence == len(sequence)


def solution_2(array, sequence):
    """
    O(n) time
    O(1) space

    """
    idx = 0
    for value in array:
        if value == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True

    return False
