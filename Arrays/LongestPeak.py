def longestPeak(array: list) -> int:
    """
    O(n) time
    O(1) space

    n is the length of the array. 
    """
    i = 1
    max_length = 0
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i + 1] < array[i]:
            left_idx = i - 1
            right_idx = i + 1
            length = 3
        else:
            i += 1
            continue
        while left_idx - 1 >= 0 and array[left_idx - 1] < array[left_idx]:
            left_idx -= 1
            length += 1
        while right_idx + 1 <= len(array) - 1 and array[right_idx + 1] < array[right_idx]:
            right_idx += 1
            length += 1
        max_length = max(length, max_length)
        i = right_idx

    return max_length
