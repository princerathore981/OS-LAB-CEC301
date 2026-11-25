# Operating Systems — Practical File

**Course:** CEC301 — Operating Systems

**Program:** B.Tech (CSE) — Third Year

**Language:** Python

**Submitted by:** Prince Rathore

**Roll No.:** 2472170

---

## About

This repository contains the practical (lab) work for **CEC301: Operating Systems**. It covers 11 programs that demonstrate core OS concepts: process management, threading, CPU scheduling, synchronization, deadlock avoidance, memory management, disk scheduling and file allocation. All programs are implemented in Python.

## List of Programs

| S.No. | Title of Program | Topic |
|-------|------------------|-------|
| 1 | Introduction to Linux System Calls, Process Creation using `fork()`, `exec()` and `wait()` | Process management |
| 2 | Thread Creation and Management using POSIX Threads (pthreads) | Threading |
| 3 | CPU Scheduling Algorithms — FCFS, SJF, Priority and Round Robin | CPU scheduling |
| 4 | Process Synchronization — Producer-Consumer Problem using Semaphores | Synchronization |
| 5 | Process Synchronization — Readers-Writers Problem using Semaphores | Synchronization |
| 6 | Dining Philosophers Problem using Semaphores | Synchronization |
| 7 | Deadlock Avoidance using Banker's Algorithm | Deadlock |
| 8 | Contiguous Memory Allocation — First Fit, Best Fit and Worst Fit | Memory management |
| 9 | Page Replacement Algorithms — FIFO, LRU and Optimal | Memory management |
| 10 | Disk Scheduling Algorithms — FCFS, SSTF, SCAN and C-SCAN | Disk management |
| 11 | File Allocation Methods — Contiguous, Linked and Indexed Allocation | File systems |

## Project Structure

```
os-practical-file/
├── README.md
├── 01_system_calls/
│   └── fork_exec_wait.py
├── 02_threads/
│   └── threads.py
├── 03_cpu_scheduling/
│   └── scheduling.py
├── 04_producer_consumer/
│   └── producer_consumer.py
├── 05_readers_writers/
│   └── readers_writers.py
├── 06_dining_philosophers/
│   └── dining_philosophers.py
├── 07_bankers_algorithm/
│   └── bankers.py
├── 08_memory_allocation/
│   └── memory_allocation.py
├── 09_page_replacement/
│   └── page_replacement.py
├── 10_disk_scheduling/
│   └── disk_scheduling.py
└── 11_file_allocation/
    └── file_allocation.py
```


## Requirements

- Python 3.8 or higher
- Linux or macOS (Program 1 uses `os.fork()`, which is not available on Windows). On Windows, use WSL.
- No third-party packages needed; the programs use only the standard library (`os`, `threading`, `time`, `collections`, etc.)

## How to Run

```bash
# Clone the repository
git clone <your-repo-url>
cd os-practical-file

# Run any program
python3 01_system_calls/fork_exec_wait.py
python3 03_cpu_scheduling/scheduling.py
```

## Concepts Covered

- **Process management:** process creation with `fork()`, replacing a process image with `exec()`, and synchronizing parent and child with `wait()`
- **Threading:** creating, running and joining threads (the Python `threading` module serves as the equivalent of POSIX pthreads)
- **CPU scheduling:** FCFS, SJF, Priority and Round Robin, with waiting time and turnaround time calculations
- **Synchronization:** semaphores and mutexes applied to the Producer-Consumer, Readers-Writers and Dining Philosophers problems
- **Deadlock avoidance:** safe-state checking with Banker's Algorithm
- **Memory management:** First Fit, Best Fit and Worst Fit allocation, and FIFO, LRU and Optimal page replacement
- **Disk scheduling:** FCFS, SSTF, SCAN and C-SCAN, with total head movement
- **File allocation:** Contiguous, Linked and Indexed methods

## Sample Output


```
Example:
Process       Burst   Waiting   Turnaround
P1            5       0         5
P2            3       5         8
Average waiting time: 2.5
```

## Notes

- Each program is self-contained and takes input from the console (or uses sample data defined in the script).
- The lab manual runs 31 pages and includes the aim, algorithm, source code and output for each program.

## Author

**Prince Rathore**

B.Tech CSE, Third Year

Roll No.: 2472170
