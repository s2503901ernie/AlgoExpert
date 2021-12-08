"""
O(n) time
O(n) space

n is the number of nodes

"""


def inOrderTraverse(tree, array: list) -> list:
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array


def preOrderTraverse(tree, array: list) -> list:
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array: list) -> list:
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)

    return array
