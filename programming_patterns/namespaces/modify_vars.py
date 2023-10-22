'''Here you will find that the f and g
functions can modify members of the list x
'''
x = [1, 2, 3]


def f():
    '''Modifies a global variable
    '''
    print(f"x before modify={x}")
    x[1] = 10
    print(f"x after modify={x}")


def g(v: list):
    '''Modifies a parameter that comes
    from a global variable
    '''
    print(f"v before modify={v}")
    v[0] = 1000
    print(f"v after modify={v}")


f()
g(x)
print(globals())
