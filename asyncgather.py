import asyncio
from time import sleep

# explain this code

async def foo(n):
    print(f"n: {n}!", flush=True)
    sleep(5)
    await asyncio.sleep(10)

async def main():
    print("Run tasks and gather...", flush=True)
    tasks = [foo(1), foo(2), foo(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())
