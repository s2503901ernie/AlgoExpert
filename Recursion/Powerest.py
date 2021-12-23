def powerset(array: list) -> list:
    """
    O(n*2^n) time
    O(n*2^n) space

    n is the length of the array.
    """
    ans = [[]]
    for ele in array:
        for i in range(len(ans)):
            ans.append(ans[i] + [ele])

    return ans


def powerset2(array: list) -> list:
    """
    * More clearly version.

    O(n*2^n) time
    O(n*2^n) space

    n is the length of the array.
    """
    ans = [[]]
    for ele in array:
        for i in range(len(ans)):
            current = ans[i]
            new_current = current + [ele]
            ans.append(new_current)

    return ans
