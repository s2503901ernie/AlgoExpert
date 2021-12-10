class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    """
    O(n) time
    O(h) space

    n is the number of nodes
    h is the height of the tree
    """

    depth, diameter = calculate(tree)

    return diameter


def calculate(tree):
    if tree is None:
        return 0, 0

    left_depth, left_max_diameter = calculate(tree.left)
    right_depth, right_max_diameter = calculate(tree.right)
    depth = max(left_depth, right_depth)
    max_diameter = max(left_depth + right_depth, left_max_diameter, right_max_diameter)

    return depth + 1, max_diameter
