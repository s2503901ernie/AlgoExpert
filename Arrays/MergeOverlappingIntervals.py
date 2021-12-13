def mergeOverlappingIntervals(intervals: list) -> list:
    """
    O(nlogn) time
    O(n) space

    n is the legnth of the intervals.
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    current_interval = sorted_intervals[0]
    for next_interval in sorted_intervals[1:]:
        if current_interval[1] >= next_interval[0]:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            ans.append(current_interval)
            current_interval = next_interval
    ans.append(current_interval)

    return ans
