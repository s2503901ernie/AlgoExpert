class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop1(head):
    """
    O(n) time
    O(n) space

    n is the length of the linked list.
    """
    board = set()
    current = head
    while current is not None:
        if current not in board:
            board.add(current)
        else:
            return current
        current = current.next
    return None


def findLoop2(head):
    """
    O(n) time
    O(1) space

    n is the length of the linked list.
    """
    if not head or not head.next:
        return None
    first = head.next
    second = head.next.next
    while first and second and second.next and first != second:
        first = first.next
        second = second.next.next

    if not first or not second or not second.next:
        return None

    first = head
    while first and second and first != second:
        first = first.next
        second = second.next

    return first
