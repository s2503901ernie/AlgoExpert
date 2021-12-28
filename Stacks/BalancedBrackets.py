def balancedBrackets(string):
    """
    O(n) time
    O(n) space

    n is the length of the string.
    """
    open_brackets = {"(", "[", "{"}
    close_brackest = {")", "]", "}"}
    match = {"(": ")", ")": "(",
             "[": "]", "]": "[",
             "{": "}", "}": "{"
             }
    stack = []
    for bracket in string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackest:
            if not stack:
                return False
            if stack.pop() != match[bracket]:
                return False

    return len(stack) == 0
