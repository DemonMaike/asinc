from multiprocessing import Process
import os

def proc_info():
    # For looking processes PID
    print('Name of module: ', __name__)
    print('PID of parents process ', os.getppid())
    print('PID of child process ', os.getpid())
    

def process():
    # Start of fucntion
    proc_info()
    

if __name__ == '__main__':
    process() # start of func
    
    p = Process(target=process) # create new process of main func
    p.start() # start of new process
    p.join()