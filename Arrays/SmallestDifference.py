def smallestDifference(arrayOne: list, arrayTwo: list) -> list:
    """
    O(nlogn + mlogm) time
    O(1) space

    """
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    min_diff = float('inf')
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayTwo[j]]
        if abs(arrayOne[i] - arrayTwo[j]) < min_diff:
            min_diff = abs(arrayOne[i] - arrayTwo[j])
            ans = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1

    return ans
