import asyncio

# create async func that print timer for choose time
async def timer(t):
    while 1:
        await asyncio.sleep(t)
        print(f'{t} is end')

# setting func for our corutines
async def main():
    tasks = [
        asyncio.create_task(timer(1)),
        asyncio.create_task(timer(5)),
        asyncio.create_task(timer(10))
    ]

    await asyncio.wait(tasks)
    
# add our main func and start event_loop
asyncio.run(main())