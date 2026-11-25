MAX = 20
class Process:
    def __init__(self, pid, at, bt, pr):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.pr = pr
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.rem = 0
def print_result(p, n):
    total_wt = 0
    total_tat = 0
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{p[i].pid}\t{p[i].at}\t{p[i].bt}\t{p[i].ct}\t{p[i].tat}\t{p[i].wt}")
        total_wt += p[i].wt
        total_tat += p[i].tat
    print(f"Average Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")
def fcfs(p, n):
    time = 0
    for i in range(n):
        if time < p[i].at:
            time = p[i].at
        time += p[i].bt
        p[i].ct = time
        p[i].tat = p[i].ct - p[i].at
        p[i].wt = p[i].tat - p[i].bt
    print_result(p, n)
def sjf(p, n):
    completed = 0
    time = 0
    done = [0] * MAX
    while completed < n:
        idx = -1
        min_bt = 10**9
        for i in range(n):
            if not done[i] and p[i].at <= time and p[i].bt < min_bt:
                min_bt = p[i].bt
                idx = i
        if idx == -1:
            time += 1
            continue
        time += p[idx].bt
        p[idx].ct = time
        p[idx].tat = p[idx].ct - p[idx].at
        p[idx].wt = p[idx].tat - p[idx].bt
        done[idx] = 1
        completed += 1
    print_result(p, n)
def priority_scheduling(p, n):
    completed = 0
    time = 0
    done = [0] * MAX
    while completed < n:
        idx = -1
        best = 10**9
        for i in range(n):
            if not done[i] and p[i].at <= time and p[i].pr < best:
                best = p[i].pr
                idx = i
        if idx == -1:
            time += 1
            continue
        time += p[idx].bt
        p[idx].ct = time
        p[idx].tat = p[idx].ct - p[idx].at
        p[idx].wt = p[idx].tat - p[idx].bt
        done[idx] = 1
        completed += 1
    print_result(p, n)
def round_robin(p, n, quantum):
    time = 0
    completed = 0
    for i in range(n):
        p[i].rem = p[i].bt
    queue = []
    front = 0
    in_queue = [0] * MAX
    # start with process(es) arriving at time 0, in PID order
    for i in range(n):
        if p[i].at <= time:
            queue.append(i)
            in_queue[i] = 1
    while completed < n:
        if front == len(queue):
            time += 1
            for i in range(n):
                 if not in_queue[i] and p[i].rem > 0 and p[i].at <= time:
                    queue.append(i)
                    in_queue[i] = 1
            continue
        idx = queue[front]
        front += 1
        slice_ = p[idx].rem if p[idx].rem < quantum else quantum
        time += slice_
        p[idx].rem -= slice_
        for i in range(n):
            if not in_queue[i] and p[i].rem > 0 and p[i].at <= time and i != idx:
                queue.append(i)
                in_queue[i] = 1
        if p[idx].rem > 0:
            queue.append(idx)
        else:
            p[idx].ct = time
            p[idx].tat = p[idx].ct - p[idx].at
            p[idx].wt = p[idx].tat - p[idx].bt
            completed += 1
            in_queue[idx] = 0
    print_result(p, n)
def main():
    n = int(input("Enter number of processes: "))
    p = []
    for i in range(n):
        at, bt, pr = map(int, input(
            f"Process {i + 1} - Arrival Time, Burst Time, Priority: ").split())
        p.append(Process(i + 1, at, bt, pr))
    print("\nMenu:\n1. FCFS\n2. SJF (Non-preemptive)")
    print("3. Priority (Non-preemptive)\n4. Round Robin")
    choice = int(input("Enter choice: "))
    if choice == 1:
        fcfs(p, n)
    elif choice == 2:
        sjf(p, n)
    elif choice == 3:
        priority_scheduling(p, n)
    elif choice == 4:
        quantum = int(input("Enter time quantum: "))
        round_robin(p, n, quantum)
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
