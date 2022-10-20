def valid_parentheses(parens):
    """Are the parentheses validly balnaced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False
    """

    visited = []

    for p in parens:
        if p == "(":
            visited.append(p)
        else:
            if len(visited) == 0:
                return False
            else:
                visited.pop()

    return len(visited) == 0