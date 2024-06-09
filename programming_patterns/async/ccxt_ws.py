# pylint: disable-all
import asyncio
import json
from pprint import pprint
from random import random
from typing import List, NoReturn

import websockets
from websockets.exceptions import ConnectionClosed, InvalidStatusCode


URI = "wss://stream.binance.com:9443/ws"
BACKOFF_MIN_SECS = 2.0
ASYNCIO_SLEEPTIME = 0.01


async def subscribe_(symbols: List, i: int = 0) -> NoReturn:
    """Subscribe to symbols"""
    backoff_delay = BACKOFF_MIN_SECS
    while True:
        try:
            async with websockets.connect(URI) as con:
                params = [f'{symbol.lower()}@kline_1m' for symbol in symbols]
                await con.send(
                    message=json.dumps({
                        "method": "SUBSCRIBE",
                        "params": params,
                        "id": i
                    })
                )
                print(f"Connection {i}: Successful")
                backoff_delay = BACKOFF_MIN_SECS
                while True:
                    msg = json.loads(await con.recv())
                    if isinstance(msg, dict):
                        if 'result' in msg:
                            if msg['result']:
                                raise ValueError("Something is wrong with received msg")
                        else:
                            data = {
                                'symbol': msg['s'],
                                'timestamp': int(msg['k']['t']),
                                'open_': msg['k']['o'],
                                'high_': msg['k']['h'],
                                'low_': msg['k']['l'],
                                'close_': msg['k']['c'],
                                'volume_': msg['k']['v'],
                            }
                            print("Data:")
                            pprint(data)
                    await asyncio.sleep(ASYNCIO_SLEEPTIME)
        except (ConnectionClosed, InvalidStatusCode) as exc:
            print(f"Connection {i}: Raised exception: {exc} - reconnecting...")
            await asyncio.sleep(backoff_delay)
            backoff_delay *= (1 + random())


async def subscribe_symbols(symbols: List, batchsize: int = 10):
    """Subscribe to symbols in batch"""
    await asyncio.gather(
        *(
            subscribe_(symbols=symbols[i:i + batchsize], i=int(i/batchsize))
            for i in range(0, len(symbols), batchsize)
        )
    )


def run_subscribe():
    """Run subscribe"""
    asyncio.run(subscribe_symbols(symbols=["ETHBTC"]))


run_subscribe()
