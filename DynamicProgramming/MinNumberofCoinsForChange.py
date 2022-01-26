def minNumberOfCoinsForChange(n, denoms):
    """
    O(nd) time
    O(n) space

    n is the amount.
    d is the number of denoms.
    """
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0
    for denom in denoms:
        for current in range(n + 1):
            if denom <= current:
                dp[current] = min(dp[current], dp[current - denom] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1
