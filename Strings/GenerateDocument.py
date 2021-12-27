def generateDocument(characters, document):
    """
    O(n + m) time
    O(c) space

    n is the length of characters.
    m is the length of document.
    c is the number of unique characters in both inputs.
    """
    board = {}
    for letter in characters:
        if letter not in board:
            board[letter] = 1
        else:
            board[letter] += 1
    for letter in document:
        if letter not in board:
            return False
        else:
            if board[letter] == 0:
                return False
            else:
                board[letter] -= 1

    return True
