"""
O(n) time
O(d) space

n is the number of nodes
d the the depth of the tree

"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):

    return validate(tree, min_value=-99999, max_value=99999)


def validate(node: BST, min_value, max_value) -> bool:
    while node is not None:
        if node.value < min_value or node.value >= max_value:
            return False
        else:
            left = validate(node.left, min_value, node.value)
            right = validate(node.right, node.value, max_value)

            return left and right

    return True
