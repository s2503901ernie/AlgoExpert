def insertionSort(array: list) -> list:
    """
    Best:
    O(n) time
    O(1) space

    Average:
    O(n^2) time
    O(1) space

    Worst:
    O(n^2) time
    O(1) space

    n is the length of the array.
    """
    for i in range(len(array)):
        j = i
        while j < 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1

    return array
