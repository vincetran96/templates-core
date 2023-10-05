import time

def timer_closure():
    now = time.time()
    def _timer():
        elapsed = time.time() - now
        print(f"Elapsed: {elapsed}")
    return _timer
