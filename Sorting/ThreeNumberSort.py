def threeNumberSort(array, order):
    """
    O(n) time
    O(1) space

    n is the length of the array.
    """
    left = 0
    for target in order:
        for right in range(left+1, len(array)):
            if array[left] == target:
                left += 1
            elif array[left] != target and array[right] == target:
                array[left], array[right] = array[right], array[left]
                left += 1

    return array
