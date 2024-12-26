import threading as th
import time

L1 = th.Lock()
L2 = th.Lock()

def task1():
    print('task1 aquring L1....')
    L1.acquire()
    print('task1 aqured L1....')
    print('task1 aquring L2...')
    L2.acquire()
    print('task1 aqured L2...')
    time.sleep(1)
    L2.release()
    L1.release()

def task2():
    print('task2 aquring L2....')
    L2.acquire()
    print('task2 aqured L2....')
    print('task2 aquring L1...')
    L1.acquire()
    print('task2 aqured L1...')
    time.sleep(1)
    L1.release()
    L2.release()
t1 = th.Thread(target=task1)
t2 = th.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print('end.....')