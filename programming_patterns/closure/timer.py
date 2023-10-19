import time


def timer_closure():
    '''This is a very basic function illustrating
    the usage of closure
    '''
    now = time.time()
    def _timer():
        elapsed = time.time() - now
        print(f"Elapsed: {elapsed}")
    return _timer
