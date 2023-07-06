import asyncio

async def timer(t):
    while 1:
        await asyncio.sleep(t)
        print(f'{t} is end')

async def main():
    tasks = [
        asyncio.create_task(timer(1)),
        asyncio.create_task(timer(5)),
        asyncio.create_task(timer(10))
    ]

    await asyncio.wait(tasks)
    

asyncio.run(main())