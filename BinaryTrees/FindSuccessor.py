class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor1(tree, node):
    """
    O(n) time
    O(n) space

    n is the number of nodes
    """
    array = []
    final_array = in_order(tree, array)
    for i, ele in enumerate(array):
        if ele == node:
            if i == len(array) - 1:
                return None
            else:
                return array[i+1]


def in_order(node, array):
    if node is not None:
        in_order(node.left, array)
        array.append(node)
        in_order(node.right, array)

    return array


def findSuccessor2(tree, node):
    """
    O(h) time
    O(1) sapce

    h is the height of the tree.
    """
    if node.right is not None:
        return find_left_child(node.right)

    return find_right_parent(node)


def find_left_child(node):
    while node.left is not None:
        node = node.left

    return node


def find_right_parent(node):
    while node.parent is not None and node.parent.right == node:
        node = node.parent

    return node.parent

