import threading
import time
 
l1 = threading.Lock()
l2 = threading.Lock()
l3 = threading.Lock()
 
def f1(name):
    print(f'thread {name}, about to lock l1')
    #Hold and Wait vermeiden(Benötigte Ressourcen am Beginn reservieren)
    with l3:
        with l1 and l2:
            print(f'thread {name}, has lock l1')
            time.sleep(0.3)
            print(f'thread {name}, about to lock l2')
            #print(f'thread {name}, run into deadLock,\nthis line will never run')
            time.sleep(0.3)
 
def f2(name):
    print(f'thread {name}, about to lock l2')
    with l3:
        with l2 and l1:
            print(f'thread {name}, has lock l2')
            time.sleep(0.3)
            print(f'thread {name}, about to lock l1')
            #print(f'thread {name}, run into deadLock,\nthis line will never run')
            time.sleep(0.3)
 
if __name__ == '__main__':
    t1=threading.Thread(target=f1, args=['t1',])
    t2=threading.Thread(target=f2, args=['t2',])
 
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("paaast")