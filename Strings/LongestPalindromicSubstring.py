def longestPalindromicSubstring(string):
    """
    O(n^2) time
    O(n^2) space

    n si the length of the string.
    """
    max_length = [0, 0]
    for i in range(len(string)):
        odd = get_length(i-1, i+1, string)
        even = get_length(i, i+1, string)
        odd_length = odd[1] - odd[0] + 1
        even_length = even[1] - even[0] + 1
        if odd_length > even_length:
            current_max = odd
        else:
            current_max = even
        max_length = max(max_length, current_max, key=lambda x: x[1] - x[0])

    return string[max_length[0]:max_length[1] + 1]


def get_length(left, right, string):
    while left >= 0 and right <= len(string) - 1:
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right - 1]
