def productSum(array):
    """
    O(n) time
    O(d) space

    n is the total number of elements in the array.
    d is the max depth of the sub-array.
    """
    return calculate(array, level=1)


def calculate(array, level):
    sums = 0
    for i in array:
        if type(i) is list:
            sums += calculate(i, level+1)
        else:
            sums += i

    return sums * level
