def validIPAddresses(string):
    """
    O(1) time
    O(1) space
    """
    ans = []
    for i in range(1, 4):
        current = ["", "", "", ""]
        if valid(string[:i]) is False:
            continue
        current[0] = string[:i]
        for j in range(i+1, i+4):
            if valid(string[i:j]) is False:
                continue
            current[1] = string[i:j]
            for k in range(j+1, j+4):
                if valid(string[j:k]) is False:
                    continue
                current[2] = string[j:k]
                if valid(string[k:]) is False:
                    continue
                current[3] = string[k:]
                ans.append(current[0] + "." + current[1] + "." + current[2] + "." + current[3])

    return ans


def valid(string):
    if not string:
        return False
    if int(string) > 255:
        return False

    return len(string) == len(str(int(string)))
