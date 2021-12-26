class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    """
    O(n + m) time
    O(1) space

    n is the length of headOne.
    m is the length of headTwo.
    """
    final = LinkedList(0)
    current = final
    current1 = headOne
    current2 = headTwo
    while current1 is not None and current2 is not None:
        if current1.value < current2.value:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1 is not None:
        current.next = current1
    else:
        current.next = current2

    return final.next
