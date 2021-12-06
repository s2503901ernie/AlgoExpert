"""
competitions
[
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

results
[0, 0, 1]
"""


def solution_1(competitions, results):
    """
    O(n) time
    O(k) space
    n: competition times
    k: teams number

    """
    board = {}
    for i, pair in enumerate(competitions):
        if results[i] == 0:
            if pair[1] in board:
                board[pair] += 3
            else:
                board[pair] = 3
        else:
            if pair[0] in board:
                board[pair] += 3
            else:
                board[pair] = 3

    return max(board, key=board.get)
