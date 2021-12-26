class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head: LinkedList, k: int) -> LinkedList:
    """
    O(n) time
    O(1) space

    n is the length of the head.
    """

    length = 0
    current = head
    while current is not None:
        length += 1
        if current.next is not None:
            current = current.next
        else:
            current.next = head
            break

    k = length - k % length
    previous = current
    current = head
    n = 0
    while n < k:
        current = current.next
        previous = previous.next
        n += 1
    previous.next = None

    return current
