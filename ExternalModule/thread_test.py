import threading
import time

def worker():
    print("Worker thread is starting.")
    time.sleep(2)
    print("Worker thread is ending.")
    
if __name__ == "__main__":
    print("Main thread is starting.")
    thread = threading.Thread(target=worker)
    thread.start()
    print("Main thread is doing other work.")
    time.sleep(1)
    print("Main thread is waiting for the worker thread to finish.")
    thread.join()
    print("Main thread is ending.")
    
#multiple threads example
def worker1():
    print("Worker 1 is starting.")
    time.sleep(2)
    print("Worker 1 is ending.")

def worker2():
    print("Worker 2 is starting.")
    time.sleep(2)
    print("Worker 2 is ending.")

if __name__ == "__main__":
    print("Main thread is starting.")
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    thread1.start()
    thread2.start()
    print("Main thread is doing other work.")
    time.sleep(1)
    print("Main thread is waiting for the worker threads to finish.")
    thread1.join()
    thread2.join()
    print("Main thread is ending.")
    
#another multiple threads example with for loop
def worker(num):
    print(f"Worker {num} is starting.")
    time.sleep(2)
    print(f"Worker {num} is ending.")

if __name__ == "__main__":
    print("Main thread is starting.")
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    print("Main thread is doing other work.")
    time.sleep(1)
    print("Main thread is waiting for the worker threads to finish.")
    for thread in threads:
        thread.join()
    print("Main thread is ending.")