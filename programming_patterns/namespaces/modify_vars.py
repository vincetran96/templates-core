'''Here you will find that the f and g
functions can modify members of the list x
'''
x = [1, 2, 3, 4]


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


def h(v: list):
    '''Modifies a slice of a parameter that comes
    from a global variable
    '''
    if len(v) < 4:
        raise ValueError
    sl = v[:5]
    sl[0] = 2000
    print(f"slice={sl}")
    print(f"v after modify of slice={v}")


f()
g(x)
h(x)
print(globals())
