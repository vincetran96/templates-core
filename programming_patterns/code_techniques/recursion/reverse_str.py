def reverse(s: str):
    if len(s) == 1:
        return s
    return s[len(s) - 1] + reverse(s[:len(s) - 1])


def reverse_1(s: str):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse("abc"))
    print(reverse_1("abc"))
