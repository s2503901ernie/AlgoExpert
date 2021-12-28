def sunsetViews(buildings, direction):
    """
    O(n) time
    O(n) space

    n is the length of the buildings.
    """
    ans = []
    if direction == "EAST":
        for i in range(len(buildings)):
            while ans and buildings[ans[-1]] <= buildings[i]:
                ans.pop()
            ans.append(i)
    else:
        for i in range(len(buildings)):
            if not ans:
                ans.append(i)
            elif buildings[i] > buildings[ans[-1]]:
                ans.append(i)

    return ans
