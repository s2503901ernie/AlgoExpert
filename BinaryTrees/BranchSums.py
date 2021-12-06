class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    final = []
    sum_up(node=root, current=0, final=final)
    return final


def sum_up(node: BinaryTree, current: int, final: list):
    if node is None:
        return
    current += node.value
    if node.left is None and node.right is None:
        final.append(current)
        return
    sum_up(node.left, current, final)
    sum_up(node.right, current, final)
