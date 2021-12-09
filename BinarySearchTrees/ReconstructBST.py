class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    """
    O(n) time
    O(n) space

    n is the number of nodes.
    """

    return construct(preOrderTraversalValues, -999999, 999999)


def construct(array, min_value, max_value):
    if len(array) == 0:
        return None
    if array[0] < min_value or array[0] >= max_value:
        return None

    added_value = array.pop(0)
    left = construct(array, min_value, added_value)
    right = construct(array, added_value, max_value)

    return BST(added_value, left, right)
