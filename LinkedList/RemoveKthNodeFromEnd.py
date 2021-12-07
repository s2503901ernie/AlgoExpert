class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    """
    O(n) time
    O(1) space

    n is the number of the nodes of the linked list
    """
    left = head
    right = head
    n = 0
    while n < k:
        n += 1
        right = right.next
    # the head is the node to be removed
    if right is None:
        head.value = head.next.value
        head.next = head.next.next

        return
    while right.next is not None:
        left = left.next
        right = right.next
    left.next = left.next.next

    return
