def numberOfWaysToTraverseGraph(width, height):
    """
    O(wh) time
    O(wh) space

    """
    matrix = [[1 for _ in range(width)] for _ in range(height)]
    for i in range(1, height):
        for j in range(1, width):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[-1][-1]
