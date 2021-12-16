def selectionSort(array):
    """
    O(n^2) time
    O(1) space
    :param array:
    :return:
    """
    current_idx = 0
    while current_idx < len(array) - 1:
        min_idx = current_idx
        for i in range(current_idx, len(array) - 1):
            if array[i] < array[min_idx]:
                min_idx = i

        array[min_idx], array[current_idx] = array[current_idx], array[min_idx]
        current_idx += 1

    return array
