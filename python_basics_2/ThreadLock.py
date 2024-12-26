import threading
import time
lock = threading.Lock()
bat = 'MRF'

def batting(name):
    global bat
    lock.acquire()
    try:
        print(name, 'starts batting using', bat)
        time.sleep(5)
        print(name, 'Out')
    finally:
        lock.release()

t1 = threading.Thread(target=batting, args=['Virat'])
t2 = threading.Thread(target=batting, args=['Sunil Narine'])

t1.start()
t2.start()