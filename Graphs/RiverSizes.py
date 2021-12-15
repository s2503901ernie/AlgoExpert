def riverSizes(matrix):
    """
    O(w*h) time
    O(w*h) space

    w is the width of the matrix.
    h is the height of the matrix.
    """
    sizes = []
    visited = [[False for col in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] is True:
                continue
            traverse(i, j, visited, matrix, sizes)

    return sizes


def traverse(i: int, j: int, visited: list, matrix: list, sizes: list):
    node_to_explore = [[i, j]]
    current_size = 0
    while len(node_to_explore) > 0:
        current = node_to_explore.pop()
        i = current[0]
        j = current[1]
        if visited[i][j] is True:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_size += 1
        neighbors = find_neighbors(i, j, visited, matrix)
        for neighbor in neighbors:
            node_to_explore.append(neighbor)

    if current_size > 0:
        sizes.append(current_size)


def find_neighbors(i, j, visited, matrix):
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
