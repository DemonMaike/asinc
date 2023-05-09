# This code preview the threading in python
# thread in this code is real thread in OS and it can look if to use command 'ps aux | grep python' and 'ps -T -p <PIDp>'

# from threading import Thread
# from time import sleep, time

# def tread_func():
#     sleep(100)
    
# tread_1 = Thread(target=tread_func)
# tread_2 = Thread(target=tread_func)

# if __name__ == '__main__':
#     tread_1.start()
#     tread_2.start()
#     tread_1.join()
#     tread_2.join()
    
    

# And now we look for memory in threads,
# it must be one for different threads,
# becouse treads works into one process and we split resoures this process
from threading import Thread

# data = dict()

# def tread_func_1():
#     data['t1'] = True
#     print(data)

# def tread_func_2():
#     data['t2'] = True
#     print(data)
    
# thread_1 = Thread(target=tread_func_1)
# thread_2 = Thread(target=tread_func_2)

# if __name__ == '__main__':
#     print(data)
#     thread_1.start()
#     thread_2.start()
#     thread_1.join()
#     thread_2.join()
    
# Output:
# {}
# {'t1': True}
# {'t1': True, 't2': True}

# and now we look on time for CPU tasks, and understed, treads are bad idea for CPU tasks

# Synchronius example

from time import time



def counter(id:int):
    i = 0
    start_time = time()
    
    while i < 50_000_000:
        i += 1
        
    print(f'{id} task worked is: {time() - start_time } sec.')
    

COUNT = 2

begin = time()
print('Start synchronius code\r')
for i in range(COUNT):
    counter(i + 1)
    
print(f'Final time for all tasks are: {time() - begin}\n')


# Example with threads
print('Start code, splits on threads')
begin_async = time()

thread_1 = Thread(target=counter, args=(1,))
thread_2 = Thread(target=counter, args=(2,))

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(f'Final time for all tasks are: {time() - begin_async}\n')    

# Output:
# Start synchronius code
# 1 task worked is: 3.034497022628784 sec.
# 2 task worked is: 2.996337652206421 sec.
# Final time for all tasks are: 6.030994892120361

# Start code, splits on threads
# 1 task worked is: 8.11415719985962 sec.
# 2 task worked is: 8.112155199050903 sec.
# Final time for all tasks are: 8.123081684112549

# For work with threads need resurses for swith between threads, so CPU tasks worked more time