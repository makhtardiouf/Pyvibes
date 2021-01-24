import asyncio


async def foo(n):
    print(f"n: {n}!", flush=True)
    await asyncio.sleep(2)  # wait before continuing

async def main():
    print("Run tasks and gather...", flush=True)
    tasks = [foo(1), foo(2), foo(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())
