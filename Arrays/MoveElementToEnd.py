def moveElementToEnd(array: list, toMove: int) -> list:
    i = 0
    j = len(array) - 1
    while i < j:
        while array[j] == toMove:
            j -= 1
            if i == j:
                break
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array
