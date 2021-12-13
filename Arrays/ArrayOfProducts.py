def arrayOfProducts1(array: list) -> list:
    """
    O(n) time
    O(n) space

    n is the length of the array.
    """
    left_product = [1 for _ in range(len(array))]
    right_product = [1 for _ in range(len(array))]
    ans = []

    current = 1
    for i in range(len(array)):
        left_product[i] = current
        current *= array[i]
    current = 1
    for i in range(len(array)-1, -1, -1):
        right_product[i] = current
        current *= array[i]
    for i in range(len(array)):
        ans.append(left_product[i] * right_product[i])

    return ans


def arrayOfProducts2(array: list) -> list:
    """
    O(n^2) time
    O(n) space

    n is the length of the array.
    """
    ans = []
    for i in range(len(array)):
        current = 1
        for j in range(len(array)):
            if i != j:
                current *= array[j]
        ans.append(current)

    return ans
