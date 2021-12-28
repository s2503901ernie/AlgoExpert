def nextGreaterElement1(array):
    """
    O(n) time
    O(n) space

    n is the length of the array.

    """
    ans = [-1] * len(array)
    stack = []
    for i in range(2*len(array)):
        idx = i % len(array)
        while stack and array[idx] > array[stack[-1]]:
            replaced_idx = stack.pop()
            ans[replaced_idx] = array[idx]

        stack.append(idx)

    return ans


def nextGreaterElement2(array):
    """
    O(n) time
    O(n) space

    n is the length of the array.
    """
    ans = [-1] * len(array)
    stack = []
    for i in range(2*len(array) - 1, -1, -1):
        idx = i % len(array)
        while stack:
            if array[idx] < stack[-1]:
                ans[idx] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(array[idx])

    return ans

