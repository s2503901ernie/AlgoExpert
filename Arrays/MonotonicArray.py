def isMonotonic(array):
    """
    O(n) time
    O(1) space

    n is the length of the array. 
    """
    increase = False
    decrease = False

    for i in range(len(array) - 1):
        if array[i+1] > array[i]:
            increase = True
        elif array[i+1] < array[i]:
            decrease = True
        else:
            continue

        if increase is True and decrease is True:
            return False

    return True
