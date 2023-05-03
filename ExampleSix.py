# работа с await и asinc

# Изначальный пример первой версии asincio, 2014 год, python v -3.4
import asyncio


#@asyncio.coroutine
async def print_nums():
    num = 1
    while 1:
        print(num)
        num += 1
        #yield from asyncio.sleep(1) # Слип работает как блокирующая функция, по этому нужно использовать ее asyinc весрию 
        await asyncio.sleep(0.2)
        
#@asyncio.coroutine
async def print_time():
    count = 0
    while 1:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        #yield from asyncio.sleep(1)
        await asyncio.sleep(0.5)
#@asyncio.coroutine 
async def main():
    #task_1 = asyncio.ensure_future(print_nums())
    #task_2 = asyncio.ensure_future(print_time())
    task_1 = asyncio.create_task(print_nums())
    task_2 = asyncio.create_task(print_time())
    
    #yield from asyncio.gather(task_1, task_2)
    await asyncio.gather(task_1,task_2)
if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())
    

# После Python -v 3.5  появились новые термины, @asyncio.corutine = async def, yield from = await
# После Python -v 3.6 ensure_future = create_task
# После Python -v 3.7 замена конструкции с loop первратилась в asincio run