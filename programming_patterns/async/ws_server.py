import asyncio
import websockets
import time


async def hello(websocket):
    while True:
        msg = f"time: {time.monotonic_ns()}"
        print(msg)
        await websocket.send(msg)
        time.sleep(1)


async def main():
    async with websockets.serve(ws_handler=hello, host="localhost", port=8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
