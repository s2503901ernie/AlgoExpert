def tandemBicycle(redShirtSpeeds: list, blueShirtSpeeds: list, fastest) -> int:
    """
    O(nlogn) time
    O(1) speed

    n is the length of the list.
    """
    if fastest is True:
        redShirtSpeeds.sort(reverse=True)
        blueShirtSpeeds.sort()
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()

    total_speed = 0
    for i in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total_speed
