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
