def solution_1(array, targetSum):
    """
    O(n^2) time
    O(n) space

    """
    i = 0
    j = 1
    while i < len(array) - 1:
        if array[i] + array[j] != targetSum:
            j += 1
            if j > len(array) - 1:
                i += 1
                j = i + 1
        else:
            return [array[i], array[j]]

    return []


def solution_2(array, targetSum):
    """
    O(n) time
    O(n) space

    """
    nums = {}
    for num in array:
        if targetSum - num in nums.keys():
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []


def solution_3(array, targetSum):
    """
    O(nlogn) time
    O(1) space

    """
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left += 1
        else:
            right -= 1
    return []
