def maxSumIncreasingSubsequence(array: list):
    """
    O(n^2) time
    O(n) space

    n is the length of the array.
    """
    ans = [num for num in array]
    sub = [[] for _ in array]
    for i in range(len(array)):
        current = array[i]
        for j in range(i):
            if current > array[j] and current + ans[j] > ans[i]:
                ans[i] = current + ans[j]
                sub[i] = sub[j].copy()
        sub[i].append(array[i])

    max_value = -float("inf")
    max_arr = []
    for arr in sub:
        if sum(arr) > max_value:
            max_value = sum(arr)
            max_arr = arr

    return [max_value, max_arr]
