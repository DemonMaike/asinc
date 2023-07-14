import asyncio


# our awaitable func
async def timer(t):
    while 1:
        await asyncio.sleep(t)
        print(f'Print for timer {t}')

# setting for event_loop
async def main():
    await asyncio.gather(
        asyncio.create_task(timer(1)),
        asyncio.create_task(timer(5)),
        asyncio.create_task(timer(10))
    )
# run event_loop with our setting func
asyncio.run(main())