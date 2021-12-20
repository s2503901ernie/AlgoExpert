class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor1(topAncestor, descendantOne, descendantTwo):
    """
    O(d^2) time
    O(d) space

    d is the depth of the tree.
    """
    ancestor1 = get_ancestors(descendantOne)
    ancestor2 = get_ancestors(descendantTwo)
    for i in ancestor1:
        for j in ancestor2:
            if i == j:
                return i


def get_ancestors(node: AncestralTree) -> list:
    ancestors = []
    while node is not None:
        ancestors.append(node)
        node = node.ancestor

    return ancestors


def getYoungestCommonAncestor2(topAncestor, descendantOne, descendantTwo):
    """
    O(d) time
    O(1) space

    d is the depth of the tree. 
    """
    depth1 = get_depth(descendantOne)
    depth2 = get_depth(descendantTwo)
    while abs(depth1 - depth2) != 0:
        if depth1 > depth2:
            descendantOne = descendantOne.ancestor
            depth1 -= 1
        else:
            descendantTwo = descendantTwo.ancestor
            depth2 -= 1

    common_ancestor = track_ancestor(descendantOne, descendantTwo)

    return common_ancestor


def get_depth(node: AncestralTree):
    depth = 0
    while node.ancestor is not None:
        depth += 1
        node = node.ancestor

    return depth


def track_ancestor(node1: AncestralTree, node2: AncestralTree):
    if node1 == node2:
        return node1

    while node1 != node2:
        node1 = node1.ancestor
        node2 = node2.ancestor

    return node1
