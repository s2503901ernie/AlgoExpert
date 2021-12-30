def subarraySort(array):
    """
    O(n) time
    O(1) space

    n is the length of the array.
    """
    min_value = float("inf")
    max_value = float("-inf")
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            min_value = min(min_value, array[i])
            max_value = max(max_value, array[i-1])
    if min_value == float("inf"):
        return [-1, -1]
    left = 0
    right = len(array) - 1
    while left < len(array):
        if array[left] > min_value:
            break
        left += 1
    while right >= 0:
        if array[right] < max_value:
            break
        right -= 1

    return [left, right]
