'''Processing
'''
from billiard import Pool


def part_crack_helper(args):
    solution = do_job(args)
    if solution:
        return True
    else:
        return False


class Worker():
    '''Terminates pool when a work finishes job
    '''
    def __init__(self, n_workers, initializer, initargs):
        self.pool = Pool(
            processes=n_workers, 
            initializer=initializer, 
            initargs=initargs
        )

    def callback(self, result):
        if result:
            self.pool.terminate()

    def process_iterable(self, func, iterable, **kwargs):
        for part in iterable:
            self.pool.apply_async(func, args=part, callback=self.callback, **kwargs)
        self.pool.close()
        self.pool.join()
