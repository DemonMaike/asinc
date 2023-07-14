# Need create a func that calculate squere from 1 to N with asyncio
import asyncio

async def square(numbers:list) -> asyncio.coroutines:
    for i in numbers:
        await asyncio.sleep(1)
        print(f'{i*2} is square of {i}')


async def main():
    await asyncio.gather(
        asyncio.create_task(square([x for x in range(0, 11)])),
        asyncio.create_task(square([x for x in range(11, 21)]))
    )

asyncio.run(main())