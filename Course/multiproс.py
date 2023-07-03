# # MULTIPROCESSING
# # Example

# from multiprocessing import Process
# import os

# def proc_info():
#     # For looking processes PID
#     print('Name of module: ', __name__)
#     print('PID of parents process ', os.getppid())
#     print('PID of child process ', os.getpid())
    

# def process():
#     # Start of fucntion
#     proc_info()
    

# if __name__ == '__main__':
#     process() # start of func
    
#     p = Process(target=process) # create new process of main func
#     p.start() # start of new process
#     p.join()
    
# # And after we see the 'p' process will created the targets process 'process'


# SPLIT MEMORY 
# Example

from multiprocessing import Process
import os

data = dict()


def proc_info():
    print('PID of process: ', os.getpid())
    print('Data: ', data)

def proc_1():
    data['proc_1'] = True
    proc_info()
    
def proc_2():
    data['proc_2'] = True
    proc_info()
    
    
if __name__ == '__main__':
    
    p1 = Process(target=proc_1)
    p1.start()
    p2 = Process(target=proc_2)
    p2.start()
    
    p1.join()
    p2.join()
    
    proc_info()

# And after started of code we looking the func proc_1 proc_2 and general proc,
# and them memory is different and locked from each ohter