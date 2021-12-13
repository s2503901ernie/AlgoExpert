def firstDuplicateValue1(array):
    """
    O(n) time
    O(n) space

    n is the length of the array.
    """
    board = set()
    for value in array:
        if value in board:
            return value
        board.add(value)

    return -1


def firstDuplicateValue2(array):
    """
    O(n) time
    O(1) space

    n is the length of the array. 
    """
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1

    return -1
