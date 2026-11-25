# Program 5
### Process Synchronization — Readers-Writers Problem using Semaphores
## Aim
To implement the first Readers-Writers problem using semaphores, allowing multiple
readers to read a shared resource concurrently while ensuring writers get exclusive
access.
## Theory
- The Readers-Writers problem models access to a shared resource (e.g., a file or
database) by multiple reader and writer threads.
- Rules: multiple readers may read simultaneously; a writer requires exclusive access
(no other reader or writer may access the resource while it writes).
- This classic (first) solution uses a semaphore 'wrt' for exclusive writer access, a
semaphore 'mutex' to protect the shared counter 'read_count', which tracks the
number of active readers. The resource is locked by the first reader and unlocked by
the last reader; this variant may starve writers.
## Program (Python)
```
import threading
import time
mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)
read_count = 0
shared_data = 0
def reader(id):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()  # first reader locks the resource
    mutex.release()
    print(f"Reader {id}: read shared_data = {shared_data}\n", end="")
    time.sleep(0.2)
    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()  # last reader unlocks the resource
    mutex.release()
def writer(id):
    global shared_data
    wrt.acquire()
    shared_data += 1
    print(f"Writer {id}: wrote shared_data = {shared_data}\n", end="")
    time.sleep(0.3)
    wrt.release()
def main():
    w = [None, None]
    r = [None] * 5
    w[0] = threading.Thread(target=writer, args=(1,))
    w[0].start()
    for i in range(5):
        r[i] = threading.Thread(target=reader, args=(i + 1,))
        r[i].start()
    w[1] = threading.Thread(target=writer, args=(2,))
    w[1].start()
    for i in range(5):
        r[i].join()
    w[0].join()
    w[1].join()
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 readers_writers.py
```
## Sample Output
```
Writer 1: wrote shared_data = 1
Reader 1: read shared_data = 1
Reader 2: read shared_data = 1
Reader 3: read shared_data = 1
Reader 4: read shared_data = 1
Reader 5: read shared_data = 1
Writer 2: wrote shared_data = 2
```
