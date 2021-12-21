def binarySearch1(array: list, target: int) -> int:
    """
    O(logn) time
    O(logn) space

    n is the length of the array.
    """
    return calculate1(0, len(array) - 1, array, target)


def calculate1(left: int, right: int, array: list, target: int) -> int:
    if left > right:
        return -1
    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return calculate1(left, middle - 1, array, target)
    else:
        return calculate1(middle + 1, right, array, target)


def binarySearch2(array: list, target: int) -> int:
    """
    O(logn) time
    O(logn) space

    n is the length of the array. 
    """
    return calculate2(0, len(array) - 1, array, target)


def calculate2(left: int, right: int, array: list, target: int) -> int:
    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1
