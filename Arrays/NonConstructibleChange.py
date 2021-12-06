def solution(coins):
    """
    O(nlogn) time
    O(1) space

    """
    current = 0
    coins.sort()
    for i in coins:
        if i > current + 1:
            return current + 1
        else:
            current += i

    return current + 1
