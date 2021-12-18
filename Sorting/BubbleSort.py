def bubbleSort(array):
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

    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]

    return array
