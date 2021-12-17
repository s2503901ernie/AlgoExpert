def classPhotos(redShirtHeights: list, blueShirtHeights: list) -> bool:
    """
    O(nlogn) time
    O(1) space

    n is the length of redShirtHeights and blueShirtHeights.
    """
    redShirtHeights.sort()
    blueShirtHeights.sort()
    r_idx = 0
    b_idx = 0
    higher = None
    while r_idx < len(redShirtHeights) and b_idx < len(blueShirtHeights):
        if redShirtHeights[r_idx] > blueShirtHeights[b_idx]:
            current = 'r'
        elif redShirtHeights[r_idx] < blueShirtHeights[b_idx]:
            current = 'b'
        else:
            return False
        if higher is None:
            higher = current
        if current != higher:
            return False
        r_idx += 1
        b_idx += 1

    return True
