def reverse(s):
    if len(s) == 1:
        return s
    return s[len(s) - 1] + reverse(s[:len(s) - 1])
