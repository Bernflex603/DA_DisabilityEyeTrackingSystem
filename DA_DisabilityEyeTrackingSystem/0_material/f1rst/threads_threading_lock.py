import threading
import time


lock = threading.Lock()

def count(sleepTime: int):
    global gtest
    global lock
    for i in range(10):
        with lock:
            x = gtest
            print(f'{gtest=}')
            time.sleep(sleepTime)
            gtest = x + 1
            
def main():
    t1 = threading.Thread(target=count, args=[1])
    t2 = threading.Thread(target=count, args=[1.5])
    t1.start()
    t2.start()
    time.sleep(20)
       