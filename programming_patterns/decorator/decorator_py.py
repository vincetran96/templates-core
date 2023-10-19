def decorator_vanilla(func):
    def wrapper_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_func


def decorator_pass_arg(n: int):
    def decorator_vanilla(func):
        def wrapper_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * n
        return wrapper_func
    return decorator_vanilla


@decorator_pass_arg(n=10)
def greet(name: str):
    return f"Hello, {name}. "


if __name__ == "__main__":
    print(greet("James"))
