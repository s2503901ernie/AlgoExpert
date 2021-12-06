"""
Test case

array
[-10, -5, 0, 5, 10]

"""


def solution_1(array):
    """
    O(nlogn) time
    O(n) space

    """
    ans = []
    for i in array:
        ans.append(i ** 2)

    ans.sort()

    return ans


def solution_2(array):
    """
    O(n) time
    O(n) space

    """
    left = 0
    right = len(array) - 1
    ans = []
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            ans.insert(0, array[right] ** 2)
            right -= 1
        else:
            ans.insert(0, array[left] ** 2)
            left += 1

    return ans
