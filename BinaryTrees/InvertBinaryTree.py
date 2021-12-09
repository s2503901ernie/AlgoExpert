def invertBinaryTree(tree):
    """
    O(n) time
    O(d) space

    n is the number of nodes
    d is the depth of tree
    """

    return swap(tree)


def swap(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    swap(tree.left)
    swap(tree.right)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None