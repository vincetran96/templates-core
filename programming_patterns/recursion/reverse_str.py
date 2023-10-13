def reverse(s: str):
    if len(s) == 1:
        return s
    return s[len(s) - 1] + reverse(s[:len(s) - 1])
