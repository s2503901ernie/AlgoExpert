def groupAnagrams(words):
    """
    O(nlogn * w) time
    O(wn) space

    n is the longest word length in words.
    w is the number of word in words.
    """
    board = {}
    ans = []
    n = 0
    for i in range(len(words)):
        sorted_word = "".join(sorted(words[i]))
        if sorted_word not in board:
            board[sorted_word] = n
            n += 1
            ans.append([words[i]])
        else:
            ans[board[sorted_word]].append(words[i])

    return ans
