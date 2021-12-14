def hasSingleCycle(array):
    """
    O(n) time
    O(1) space

    n is the length of the array. 
    """

    n = 0
    i = 0
    while n < len(array):
        i += array[i]
        i = i % len(array)
        n += 1
        if i == 0:
            break

    return n == len(array) and i == 0
