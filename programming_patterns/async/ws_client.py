import asyncio
import websockets
import time


def process(msg):
    print(f"Processing msg: {msg}")
    time.sleep(10)


async def hello():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            async for msg in websocket:
                process(msg)
    except (Exception, ):
        return


if __name__ == "__main__":
    asyncio.run(hello())
