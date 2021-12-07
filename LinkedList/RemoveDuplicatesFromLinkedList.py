class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def solution_1(linkedList: LinkedList) -> LinkedList:
    """
    O(n) time
    O(1) space

    """
    current = linkedList
    while current is not None:
        while current.next is not None and current.value == current.next.value:
            current.next = current.next.next
        current = current.next

    return linkedList


def solution_2(linkedList: LinkedList) -> LinkedList:
    """
    O(n) time
    O(1) space

    """
    current = linkedList
    while current is not None:
        next_node = current.next
        while next_node is not None and current.value == next_node.value:
            next_node = next_node.next

        current.next = next_node
        current = current.next

    return linkedList
