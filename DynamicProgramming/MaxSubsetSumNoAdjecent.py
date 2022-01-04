def maxSubsetSumNoAdjacent(array: list):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    previous = array[0]
    current_max = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(current_max, previous + array[i])
        previous = current_max
        current_max = current

    return current_max
