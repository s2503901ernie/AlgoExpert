# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        """
        O(v + e) time
        O(v) space

        v is the number of vertices.
        e is the number of edges.
        """
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array
