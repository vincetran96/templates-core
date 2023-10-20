x = [1, 2, 3]


def f():
    print(f"x before modify={x}")
    x[1] = 10
    print(f"x after modify={x}")


f()
print(globals())
