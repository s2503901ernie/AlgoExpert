def removeIslands(matrix: list) -> list:
    """
    O(wh) time
    O(wh) space

    w is the width of the matrix.
    h is the height of the matrix.
    """
    visited = [[False for _ in row] for row in matrix]
    land = [[False for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix) - 1:
                traverse(i, j, visited, land, matrix)
            else:
                if j == 0 or j == len(matrix[i]) - 1:
                    traverse(i, j, visited, land, matrix)
                else:
                    continue

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if land[i][j] is False and matrix[i][j] == 1:
                matrix[i][j] = 0

    return matrix


def traverse(i: int, j: int, visited: list, land: list, matrix: list):
    queue = [[i, j]]
    while len(queue) > 0:
        current = queue.pop()
        i = current[0]
        j = current[1]
        if visited[i][j] is True:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        else:
            land[i][j] = True
        neighbors = get_neighbors(i, j, visited, matrix)
        for neighbor in neighbors:
            queue.append(neighbor)


def get_neighbors(i: int, j: int, visited: list, matrix: list):
    neighbors = []
    if i > 0 and visited[i-1][j] is False:
        neighbors.append([i-1, j])
    if i < len(matrix) - 1 and visited[i+1][j] is False:
        neighbors.append([i+1, j])
    if j > 0 and visited[i][j-1] is False:
        neighbors.append([i, j-1])
    if j < len(matrix[i]) - 1 and visited[i][j+1] is False:
        neighbors.append([i, j+1])

    return neighbors
