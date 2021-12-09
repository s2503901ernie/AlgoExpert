class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    """
    O(n) time
    O(n) space

    n is the number of nodes
    """
    final_array = in_order(tree, [])

    return final_array[-k]


def in_order(tree, array: list) -> list:
    if tree is not None:
        in_order(tree.left, array)
        array.append(tree.value)
        in_order(tree.right, array)

    return array
