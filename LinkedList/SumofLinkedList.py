class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    """
    O(m + n) time
    O(max(m, n)) space

    m is the length of the linkedListOne.
    n is the length of the linkedListTwo.
    """
    # calculate linkedListOne sum value
    sum1 = 0
    n = 0
    current = linkedListOne
    while current is not None:
        sum1 += current.value * 10**n
        current = current.next
        n += 1
    # calculate linkedListTwo sum value
    sum2 = 0
    n = 0
    current = linkedListTwo
    while current is not None:
        sum2 += current.value * 10**n
        current = current.next
        n += 1

    # calculate sum value
    sum_value = sum1 + sum2
    head = LinkedList(sum_value % 10)
    current = head
    sum_value = sum_value // 10
    while sum_value > 0:
        current.next = LinkedList(sum_value % 10)
        current = current.next
        sum_value = sum_value // 10

    return head
