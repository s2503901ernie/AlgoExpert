def firstNonRepeatingCharacter(string):
    """
    O(n) time
    O(1) space

    n is the length of the string.
    1 is because there are only 26 alphabet.
    """
    board = {}
    for letter in string:
        if letter not in board:
            board[letter] = 1
        else:
            board[letter] += 1

    for i in range(len(string)):
        if board[string[i]] == 1:
            return i

    return -1
