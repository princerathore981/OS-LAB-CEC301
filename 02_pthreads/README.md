# Program 2
### Thread Creation and Management using POSIX Threads(pthreads)
## Aim
To understand the concept of threads and write a multithreaded Python program using
the POSIX thread (pthread) library to create, synchronize and join threads.
## Theory
- A thread is the smallest unit of CPU execution within a process. Multiple threads
within the same process share the same address space (code, data, heap and open
files) but have their own stack, program counter and registers.
- POSIX threads (pthreads) is a standard threading API for UNIX-like systems. Key
functions include pthread_create() to create a new thread, pthread_join() to wait for
a thread to finish, and pthread_exit() to terminate a thread.
- Multithreading improves responsiveness and allows parallel execution of
independent tasks on multicore processors, but requires synchronization when
threads share data.
## Program (Python)
```
import threading
NUM_THREADS = 4
def sum_array(p):
    """Thread function: p holds the argument (start, end) and the result (sum)."""
    p["sum"] = 0
    for i in range(p["start"], p["end"]):
        p["sum"] += i
    print(f"Thread {threading.get_ident() % 100000}: "
          f"sum[{p['start']}..{p['end']}) = {p['sum']}\n", end="")
def main():
    n = 1000000
    chunk = n // NUM_THREADS
    total = 0
    threads = []
    data = []
    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        data.append({"start": start, "end": end, "sum": 0})
        t = threading.Thread(target=sum_array, args=(data[i],))
        threads.append(t)
        t.start()
    for i in range(NUM_THREADS):
        threads[i].join()
        total += data[i]["sum"]
    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {total}")
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 thread_sum.py
```
## Sample Output
```
Thread 23841: sum[0..250000) = 31249875000
Thread 23842: sum[250000..500000) = 93749875000
Thread 23843: sum[500000..750000) = 156249875000
Thread 23844: sum[750000..1000000) = 218749875000
Total sum (0 to 999999) computed using 4 threads = 499999500000
```
