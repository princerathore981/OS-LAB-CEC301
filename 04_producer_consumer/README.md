# Program 4
### Process Synchronization — Producer-Consumer Problem using Semaphores
## Aim
To implement the classical Producer-Consumer (Bounded Buffer) problem using POSIX
semaphores and threads to achieve mutual exclusion and synchronization.
## Theory
- The Producer-Consumer problem involves two types of processes/threads sharing a
fixed-size buffer: producers add items, and consumers remove them.
- Synchronization must ensure the producer does not add to a full buffer and the
consumer does not remove from an empty buffer, and that access to the shared
buffer is mutually exclusive.
- This is solved using three semaphores: 'empty' (counts empty slots, initialized to
buffer size), 'full' (counts filled slots, initialized to 0), and 'mutex' (binary semaphore
for mutual exclusion, initialized to 1).
## Program (Python)
```
import threading
import time
BUFFER_SIZE = 5
ITEMS = 10
buffer = [0] * BUFFER_SIZE
in_pos = 0
out_pos = 0
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)
def producer():
    global in_pos
    for i in range(1, ITEMS + 1):
        empty.acquire()
        mutex.acquire()
        buffer[in_pos] = i
        print(f"Producer produced item {i} at slot {in_pos}")
        in_pos = (in_pos + 1) % BUFFER_SIZE
        mutex.release()
        full.release()
        time.sleep(0.1)
def consumer():
    global out_pos
    for i in range(1, ITEMS + 1):
        full.acquire()
        mutex.acquire()
        item = buffer[out_pos]
        print(f"\t\tConsumer consumed item {item} from slot {out_pos}")
        out_pos = (out_pos + 1) % BUFFER_SIZE
        mutex.release()
        empty.release()
        time.sleep(0.15)
def main():
    prod = threading.Thread(target=producer)
    cons = threading.Thread(target=consumer)
    prod.start()
    cons.start()
    prod.join()
    cons.join()
    print("All items produced and consumed.")
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 producer_consumer.py
```
## Sample Output
```
Producer produced item 1 at slot 0
Producer produced item 2 at slot 1
        Consumer consumed item 1 from slot 0
Producer produced item 3 at slot 2
        Consumer consumed item 2 from slot 1
...
All items produced and consumed.
```
