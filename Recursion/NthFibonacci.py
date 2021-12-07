def solution_1(n):
    """
    O(n) time
    O(1) space

    """
    idx1 = 0
    idx2 = 1
    if n == 1:
        return idx1
    if n == 2:
        return idx2
    for i in range(2, n):
        new = idx1 + idx2
        idx1 = idx2
        idx2 = new

    return idx2


def solution_2(n):
    """
    O(2^n) time
    O(n) space


    """
    if n == 1:
        return 0
    if n == 2:
        return 1

    return solution_2(n-1) + solution_2(n-2)
