"""
O(n) time
O(h) space

n is the number of the nodes
h is the height of the tree


"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):

    return sum_up(root, depth=0)


def sum_up(node, depth):
    if node is None:
        return 0

    return depth + sum_up(node.left, depth + 1) + sum_up(node.right, depth + 1)
