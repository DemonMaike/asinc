# This code preview the treading in python
# tread in this code is real tread in OS and it can look if to use command 'ps aux | grep python' and 'ps -T -p <PIDp>'

from threading import Thread
from time import sleep, time

def tread_func():
    sleep(100)
    
tread_1 = Thread(target=tread_func)
tread_2 = Thread(target=tread_func)

if __name__ == '__main__':
    tread_1.start()
    tread_2.start()
    tread_1.join()
    tread_2.join()