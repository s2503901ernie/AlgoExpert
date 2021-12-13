def spiralTraverse(array: list) -> list:

    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1
    ans = []
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end + 1):
            ans.append(array[row_start][col])
        for row in range(row_start, row_end + 1):
            ans.append(array[row][col_end])
        for col in range(col_end - 1, col_start - 1, -1):
            if len(ans) == len(array) * len(array[0]):
                break
            ans.append(array[row_end][col])
        for row in range(row_end - 1, row_start, -1):
            if len(ans) == len(array) * len(array[0]):
                break
            ans.append(array[row][col_start])
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return ans
