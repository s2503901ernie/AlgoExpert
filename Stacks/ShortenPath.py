def shortenPath(path):
    """
    O(n) time
    O(n) space

    n is the length of the path.
    """
    paths = path.split("/")
    current = []
    if path[0] == "/":
        current.append("/")
    for i in paths:
        if i == "." or i == "":
            continue
        if i == "..":
            if len(current) == 1 and current[0] == "/":
                continue
            elif len(current) == 0:
                current.append(i)
            elif current[-1] == "..":
                current.append(i)
            else:
                current.pop()
        else:
            current.append(i)
    ans = ""
    for i in current:
        ans += i + "/"
    if path[0] == "/":
        ans = ans[1:]
    if path[-1] != "/" and len(ans) > 1:
        ans = ans[:-1]

    return ans
