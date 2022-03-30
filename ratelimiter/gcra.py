import time
import asyncio
import random
from collections import deque


class GCRARateLimiter:
    '''Async rate-limiter using the GCRA algorithm

    Applicable for rate-limiting requests to an API

    See GCRA explanation: https://blog.ian.stapletoncordas.co/2018/12/understanding-generic-cell-rate-limiting.html

    With reference to: https://github.com/hallazzang/asyncio-throttle
    '''
    def __init__(
        self,
        rate_limit: float,
        period: float=1.0,
    ):
        '''
        :params:
            `rate_limit_key`: unique key for this rate limiter
            `rate_limit`:
            `period`:
            `redis_client`:
        '''
        if rate_limit <= 0:
            raise ValueError("param rate_limit must be greater than 0")
        self.rate_limit = rate_limit
        self.period = period
        self.increment = self.period / self.rate_limit
        self.timestamp = None
        # self.tasks = deque()
   
    def _is_limited(self):
        '''Checks if the requesting function is rate-limited

        Source: https://dev.to/astagi/rate-limiting-using-python-and-redis-58gk
        '''
        now = time.time() # maybe consider time.monotonic()
        try:
            if not self.timestamp:
                self.timestamp = now
            tat = max(self.timestamp, now)
            allowed_at = tat + self.increment - self.period
            if now >= allowed_at:
                new_tat = tat + self.increment
                self.timestamp = new_tat
                print(f"Request allowed at {now}, allowed ts at {allowed_at}")
                return (False, None)
            print(f"Request rate-limited at {now}, allowed ts at {allowed_at}, wait for {allowed_at - now}")
            return (True, allowed_at - now)
        except Exception as exc:
            print(f"GCRARateLimiter: EXCEPTION: {exc}")
            return (True, self.increment)

    async def wait(self):
        '''API call to wait until the requesting function is not rate-limited
        '''

        while True:
            limited, retry_after = self._is_limited()
            if not limited:
                break
            await asyncio.sleep(retry_after)
        
    async def __aenter__(self):
        await self.wait()

    async def __aexit__(self, exc_type, exc, tb):
        pass


# Test run
async def worker(worker_no: int, throttler: GCRARateLimiter, n_repeat: int):
    for _ in range(n_repeat):
        # await asyncio.sleep(random.random() * 2)
        async with throttler:
            print(f"Worker {worker_no} run! @ {time.time()}")


async def run():
    throttler = GCRARateLimiter(10, 1)
    tasks = [
        loop.create_task(worker(no, throttler, 50))
        for no in range(5)
    ]
    await asyncio.wait(tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
