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

data = dict()

def tread_func_1():
    data['t1'] = True
    print(data)

def tread_func_2():
    data['t2'] = True
    print(data)
    
thread_1 = Thread(target=tread_func_1)
thread_2 = Thread(target=tread_func_2)

if __name__ == '__main__':
    print(data)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    
# Output:
# {}
# {'t1': True}
# {'t1': True, 't2': True}