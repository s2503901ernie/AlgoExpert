def getPermutations(array: list) -> list:
    """
    O(n*n!) time
    O(n*n!) space

    n is the length of the array.

    Explanation:
    https://www.geeksforgeeks.org/time-complexity-permutations-string/
    """
    if not array:
        return []
    ans = []
    helper(array=array, current=[], ans=ans)

    return ans


def helper(array: list, current: list, ans: list) -> None:
    if len(array) == 0:
        ans.append(current)
    for i in range(len(array)):
        num = array[i]
        remain_array = array[:i] + array[i+1:]
        new_current = current + [num]
        helper(remain_array, new_current, ans)
