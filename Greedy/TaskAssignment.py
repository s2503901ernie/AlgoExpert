def taskAssignment(k, tasks):
    """
    O(nlogn) time
    O(n) space

    n is the length of the tasks.
    """

    idx_array = []
    ans = []
    for i in range(len(tasks)):
        idx_array.append(i)
    sorted_idx_array = [idx for _, idx in sorted(zip(tasks, idx_array), key=lambda x: x[0])]
    left = 0
    right = len(tasks) - 1
    while left < right:
        ans.append([sorted_idx_array[left], sorted_idx_array[right]])

    return ans
