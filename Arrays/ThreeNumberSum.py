def threeNumberSum(array, targetSum) -> list:
    """
    O(n^2) time
    O(n) space

    n is the length of the array.
    """
    array.sort()
    left = 0
    middle = left + 1
    right = len(array) - 1
    ans = []
    while left < right - 1:
        while middle < right:
            if array[left] + array[middle] + array[right] == targetSum:
                ans.append([array[left], array[middle], array[right]])
                middle += 1
            elif array[left] + array[middle] + array[right] < targetSum:
                middle += 1
            else:
                right -= 1
        left += 1
        middle = left + 1
        right = len(array) - 1

    return ans
