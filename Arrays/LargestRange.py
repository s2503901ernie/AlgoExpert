def largestRange1(array: list):
    """
    O(nlogn) time
    O(1) space

    n is the length of the array.
    """
    array.sort()
    start = array[0]
    ans = [start, start]
    max_length = 1
    length = 1
    for i in range(1, len(array)):
        diff = array[i] - array[i-1]
        if diff == 1:
            length += 1
            if length > max_length:
                max_length = length
                ans = [start, array[i]]
        elif diff == 0:
            continue
        else:
            length = 1
            start = array[i]

    return ans


def largestRange2(array: list):
    """
    O(n) time
    O(n) space

    n is the length of the array. 
    """
    board = {}
    max_length = 1
    ans = [array[0], array[0]]
    for num in array:
        board[num] = True
    for num in array:
        if board[num] is False:
            continue
        board[num] = False
        length = 1
        left = num - 1
        right = num + 1
        while left in board:
            board[left] = False
            length += 1
            left -= 1
        while right in board:
            board[right] = False
            length += 1
            right += 1
        if length > max_length:
            max_length = length
            ans = [left + 1, right - 1]

    return ans
