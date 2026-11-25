# Program 6
### Dining Philosophers Problem using Semaphores
## Aim
To implement the Dining Philosophers problem using semaphores in a way that avoids
deadlock, illustrating concurrency control among multiple processes sharing limited
resources (forks).
## Theory
- Five philosophers sit around a table with five forks (one between each pair). Each
philosopher alternately thinks and eats; to eat, a philosopher needs both the left and
right fork.
- If every philosopher picks up the left fork first, all may simultaneously hold one fork
and wait forever for the right fork — a circular wait, causing deadlock.
- Deadlock is avoided here by allowing at most (N-1) philosophers to try to pick up
forks at the same time, using a counting semaphore, which breaks the circular-wait
condition.
## Program (Python)
```
import threading
import time
N = 5
forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # allows at most N-1 philosophers to sit and pick up forks
def philosopher(id):
    left = id
    right = (id + 1) % N
    for cycle in range(2):
        print(f"Philosopher {id} is thinking\n", end="")
        time.sleep(0.1)
        room.acquire()          # enter the "room" - avoids deadlock
        forks[left].acquire()   # pick up left fork
        forks[right].acquire()  # pick up right fork
        print(f"Philosopher {id} is eating (fork {left} and fork {right})\n", end="")
        time.sleep(0.15)
        forks[right].release()
        forks[left].release()
        room.release()
        print(f"Philosopher {id} finished eating and put down forks\n", end="")
def main():
    philo = []
    for i in range(N):
        t = threading.Thread(target=philosopher, args=(i,))
        philo.append(t)
        t.start()
    for i in range(N):
        philo[i].join()
if __name__ == "__main__":
    main()

```
## Compilation & Execution
```
python3 dining_philosophers.py
```
## Sample Output
```
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 0 is eating (fork 0 and fork 1)
Philosopher 2 is eating (fork 2 and fork 3)
Philosopher 0 finished eating and put down forks
Philosopher 1 is eating (fork 1 and fork 2)
...
```
