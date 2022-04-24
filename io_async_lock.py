
# https://docs.python.org/3.5/whatsnew/3.5.html
# Asynchronous context managers

import asyncio

async def runner(name, lock):
    print(f'runner {name}: waiting for lock')

    async with lock:
        print(f'runner {name}: holding the lock')
        await asyncio.sleep(1)
        print(f'runner {name}: releasing the lock')

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
runners = asyncio.gather(runner("Cruiser", lock), runner("F-16 Jet", lock), runner("Honda", lock))

try:
    loop.run_until_complete(runners)
finally:
    loop.close()