import threading
import time
def task1():
    for i in range(0, 10):
    #     print(i)
        print(threading.current_thread().getName(),':',i)
        
def task2():
    for i in range(1, 27):
        print(chr(i + 64))
        time.sleep(0.5)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.setName('ram')
t1.setName('kunal')
t1.start()
#t1.join()
t1.start()