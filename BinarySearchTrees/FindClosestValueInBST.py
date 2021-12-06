class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution1(BST):
    """
    Average case:
    O(logn) time
    O(1) space

    Worst case (highly skewed):
    O(n) time
    O(1) space

    n is the number of the nodes

    """
    def findClosestValueInBst(self, tree: BST, target: int) -> int:

        return self.finder(tree, target, tree.value)

    def finder(self, tree: BST, target: int, closest: int):
        current = tree
        while current is not None:
            if abs(current.value - target) < abs(closest - target):
                closest = current.value
            if target > current.value:
                current = current.right
            elif target < current.value:
                current = current.left
            else:
                break

        return closest


class Solution2(BST):
    """
    Average:
    O(logn) time
    O(logn) space

    Worst (highly skewed):
    O(n) time
    O(n) space

    n is the number of the nodes


    """
    def findClosestValueInBst(self, tree: BST, target: int) -> int:

        return self.finder(tree, target, tree.value)

    def finder(self, tree: BST, target: int, closest: int):
        if tree is None:
            return closest
        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value
        if target > tree.value:
            return self.finder(tree.right, target, closest)
        elif target < tree.value:
            return self.finder(tree.left, target, closest)
        else:
            return closest
