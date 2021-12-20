def runLengthEncoding(string):
    """
    O(n) time
    O(n) space

    n is the length of the string.
    """
    length = 1
    previous = string[0]
    ans = ""

    for i in string[1:]:
        if i == previous:
            length += 1
        else:
            ans += str(length) + previous
            length = 1
            previous = i
        if length > 9:
            ans += str(9) + previous
            length = 1
            previous = i

    ans += str(length) + string[-1]

    return ans
