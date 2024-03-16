print(dir(__builtins__))


x = "global"


def f(n):
    x = "enclosing"
    
    def g():
        x = "local"
        print(f"x={x}")
        print(locals())

    g()


f("enclosing")

print(globals())
print(f"x is globals()['x']: {x is globals()['x']}")
