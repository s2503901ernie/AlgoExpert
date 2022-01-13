def numberOfWaysToMakeChange(n, denoms):
    """
    O(nd) time
    O(n) space

    n is the number.
    d is the denom type number.
    """
    ans = [0 for i in range(n+1)]
    ans[0] = 1
    for denom in denoms:
        for i in range(len(ans)):
            if denom <= i:
                ans[i] += ans[i-denom]

    return ans[-1]
