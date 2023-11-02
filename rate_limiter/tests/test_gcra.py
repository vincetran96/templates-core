import time
import asyncio
import pytest
from collections import deque
from rate_limiter.gcra import GCRARateLimiter


class TestGCRA:
    async def worker(self, throttler: GCRARateLimiter, logs):
        try:
            while True:
                async with throttler:
                    logs.append(time.time())
                await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            pass

    @pytest.mark.parametrize(
        "rate_limit, num_workers",
        [(6, 5), (20, 35), (50, 100)]
    )
    @pytest.mark.asyncio
    async def test_rate_limiting(self, rate_limit, num_workers):
        throttler = GCRARateLimiter(rate_limit)
        logs = deque()

        tasks = [
            asyncio.ensure_future(self.worker(throttler, logs))
            for _ in range(num_workers)
        ]

        start = time.time()
        while True:
            now = time.time()
            if now - start >= 5.0:
                break

            while logs:
                if now - logs[0] > 1.0:
                    logs.popleft()
                else:
                    break

            assert len(logs) <= rate_limit

            await asyncio.sleep(0.05)

        for task in tasks:
            task.cancel()
