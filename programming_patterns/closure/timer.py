import time


def timer_closure():
    """This is a very basic function illustrating
    the usage of closure

    Usage:
    - Create a variable using this function
    - Then call the variable to see the time elapsed
    """
    now = time.time()
    def _timer():
        elapsed = time.time() - now
        print(f"Elapsed: {elapsed}")
    return _timer


if __name__ == "__main__":
    timer = timer_closure()
    time.sleep(5)
    timer()
