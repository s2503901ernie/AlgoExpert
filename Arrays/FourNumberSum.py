def fourNumberSum(array, targetSum):
    """
    Average:
    O(n^2) time
    O(n^2) space

    Worst:
    O(n^3) time
    O(n^2) space
    """
    pairs = {}
    ans = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current = array[i] + array[j]
            diff = targetSum - current
            if diff in pairs:
                for pair in pairs[diff]:
                    ans.append(pair + [array[i], array[j]])
        for k in range(i):
            current = array[i] + array[k]
            if current not in pairs:
                pairs[current] = [[array[i], array[k]]]
            else:
                pairs[current].append([array[i], array[k]])

    return ans
