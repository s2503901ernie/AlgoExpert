def minimumWaitingTime1(queries):
    """
    O(nlogn) time
    O(1) sapce

    n is the length of the queries.
    """
    queries.sort(reverse=True)
    ans = 0
    for i, ele in enumerate(queries):
        ans += i * ele

    return ans


def minimumWaitingTime2(queries):
    """
    O(nlogn) time
    O(1) space

    n is the length of the queries. 
    """
    queries.sort()
    ans = 0
    for i in queries[:-1]:
        ans += sum(queries[:i+1])

    return ans
