class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes1(nodeOne: BST, nodeTwo: BST, nodeThree: BST):
    """
    O(h) time
    O(h) space

    h is the height of the BST.
    """
    if is_descendant1(nodeOne, nodeTwo) is True:
        return is_descendant1(nodeTwo, nodeThree)
    else:
        return is_descendant1(nodeThree, nodeTwo)


def is_descendant1(node: BST, target: BST):
    if node is not None:
        if node.value == target.value:
            return True
        elif target.value < node.value:
            return is_descendant1(node.left, target)
        else:
            return is_descendant1(node.right, target)

    return False


def validateThreeNodes2(nodeOne: BST, nodeTwo: BST, nodeThree: BST):
    """
    O(h) time
    O(1) space

    h is the height of the BST. 
    """
    if is_descendant2(nodeOne, nodeTwo) is True:
        return is_descendant2(nodeTwo, nodeThree)
    else:
        return is_descendant2(nodeThree, nodeTwo)


def is_descendant2(node: BST, target: BST):
    while node is not None:
        if node == target:
            return True
        elif target.value < node.value:
            node = node.left
        else:
            node = node.right

    return False


