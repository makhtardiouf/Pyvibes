
# https://docs.python.org/3.5/whatsnew/3.5.html
# Asynchronous context managers

import asyncio

async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))

    async with lock:
        print('coro {}: holding the lock'.format(name))
        await asyncio.sleep(1)
        print('coro {}: releasing the lock'.format(name))

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
coros = asyncio.gather(coro("Test", lock), coro(1, lock), coro(2, lock))

try:
    loop.run_until_complete(coros)
finally:
    loop.close()