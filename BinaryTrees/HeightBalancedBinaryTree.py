class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    """
    O(n) time
    O(h) space

    n is the number of nodes.
    h is the height of the tree.
    """
    if_balanced, detph = find_depth(tree)

    return if_balanced


def find_depth(node):
    if node is None:
        return True, 0
    left_balanced, left_depth = find_depth(node.left)
    right_balanced, right_detph = find_depth(node.right)
    if abs(left_depth - right_detph) > 1:
        if_balanced = False
    else:
        if_balanced = True
    depth = max(left_depth, right_detph)
    if_balanced = if_balanced and (left_balanced and right_balanced)

    return if_balanced, depth + 1
