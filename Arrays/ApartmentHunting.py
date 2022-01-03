def apartmentHunting1(blocks, reqs):
    """
    O(n^2*r) time
    O(nr) space

    n is the length of the blocks.
    r is the length of the reqs.
    """
    board = {}
    for idx in range(len(blocks)):
        board[idx] = []
        for req in reqs:
            min_distance = float("inf")
            for i in range(len(blocks)):
                if blocks[i][req] is True:
                    if abs(i - idx) < min_distance:
                        min_distance = abs(i - idx)
            board[idx].append(min_distance)

    min_distance = float("inf")
    for key in board:
        if max(board[key]) < min_distance:
            min_distance = max(board[key])
            ans = key

    return ans


def apartmentHunting2(blocks, reqs):
    """
    O(nr) time
    O(nr) space

    n is the length of the blocks.
    r is the length of the reqs.
    """
    board = {}
    for req in reqs:
        board[req] = [0 for _ in blocks]
        closest_idx = float("inf")
        for i in range(len(blocks)):
            if blocks[i][req] is True:
                closest_idx = i
            board[req][i] = abs(i - closest_idx)

        closest_idx = float("inf")
        for i in range(len(blocks) - 1, -1, -1):
            if blocks[i][req] is True:
                closest_idx = i
            board[req][i] = min(board[req][i], abs(i - closest_idx))

    min_distance = float("inf")
    for i in range(len(blocks)):
        current = []
        for key in board:
            current.append(board[key][i])
        if max(current) < min_distance:
            min_distance = max(current)
            ans = i

    return ans
