class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst_1(array):
    return solution_1(array)


def minHeightBst_2(array):
    return solution_2(None, array)


def minHeightBst_3(array):
    mid = len(array) // 2
    bst = BST(array[mid])
    solution_3(bst, array[:mid])
    solution_3(bst, array[mid+1:])

    return bst


def solution_1(array):
    """
    O(n) time
    O(n) space

    n is the length of array
    """
    if len(array) == 0:
        return None
    mid = len(array) // 2
    bst = BST(array[mid])
    bst.left = solution_1(array[:mid])
    bst.right = solution_1(array[mid+1:])

    return bst


def solution_2(node, array):
    """
    O(nlogn) time
    O(n) space

    * log n is because of insert method combined with n nodes, which makes nlogn
    n is the length of array
    """
    if len(array) == 0:
        return
    mid = len(array) // 2
    if node is None:
        node = BST(array[mid])
    else:
        node.insert(array[mid])
    solution_2(node, array[:mid])
    solution_2(node, array[mid+1:])

    return node


def solution_3(node, array):
    """
    O(nlogn) time
    O(n) space

    * log n is because of insert method combined with n nodes, which makes nlogn
    n is the length of array
    """
    if len(array) == 0:
        return
    mid = len(array) // 2
    node.insert(array[mid])
    solution_3(node, array[:mid])
    solution_3(node, array[mid+1:])

    return
