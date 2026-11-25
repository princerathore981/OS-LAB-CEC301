# Program 7
### Deadlock Avoidance using Banker's Algorithm
## Aim
To implement the Banker's Algorithm to check whether a system is in a safe state, and
to simulate resource allocation requests, thereby avoiding deadlock.
## Theory
- The Banker's Algorithm is a deadlock-avoidance algorithm that tests whether
granting a resource request leaves the system in a safe state before actually
allocating resources.
- It uses four data structures: Available (resources currently free), Max (maximum
demand of each process), Allocation (resources currently allocated to each process),
and Need = Max − Allocation.
- The Safety Algorithm finds a sequence in which all processes can finish without
deadlock by repeatedly finding a process whose Need can be satisfied by Available,
then simulating its completion (adding its allocation back to Available).
- The Resource-Request Algorithm grants a request only if the resulting state
(obtained by tentatively allocating) is still safe; otherwise the requesting process
must wait.
## Program (Python)
```
P = 5  # number of processes
R = 3  # number of resource types
available = [0] * R
maximum = [[0] * R for _ in range(P)]
allocation = [[0] * R for _ in range(P)]
need = [[0] * R for _ in range(P)]
_tokens = []
def read_ints(count, prompt=""):
    """scanf-style input: read `count` integers (they may span several lines)."""
    while len(_tokens) < count:
        _tokens.extend(input(prompt).split())
        prompt = ""
    values = [int(t) for t in _tokens[:count]]
    del _tokens[:count]
    return values
def calculate_need():
    for i in range(P):
        for j in range(R):
            need[i][j] = maximum[i][j] - allocation[i][j]
def is_safe():
    """Returns (True, safe_sequence) if the state is safe, else (False, [])."""
    work = available[:]
    finish = [0] * P
    safe_seq = []
    while len(safe_seq) < P:
        found = 0
        for i in range(P):
            if not finish[i]:
                j = 0
                while j < R:
                    if need[i][j] > work[j]:
                        break
                    j += 1
                if j == R:
                    for k in range(R):
                        work[k] += allocation[i][k]
                    safe_seq.append(i)
                    finish[i] = 1
                    found = 1
        if not found:
            return False, []  # no process could proceed: unsafe
    return True, safe_seq
def request_resources(pid, request):
    for j in range(R):
        if request[j] > need[pid][j]:
            print("Error: process has exceeded its maximum claim.")
            return 0
        if request[j] > available[j]:
            print("Request denied: not enough resources available.")
            return 0
    # tentatively allocate
    for j in range(R):
        available[j] -= request[j]
        allocation[pid][j] += request[j]
        need[pid][j] -= request[j]
    safe, _ = is_safe()
    if safe:
        print("Request can be granted safely.")
        return 1
    else:
        # rollback
        for j in range(R):
            available[j] += request[j]
            allocation[pid][j] -= request[j]
            need[pid][j] += request[j]
        print("Request denied: would lead to an unsafe state.")
        return 0
def main():
    global available
    available[:] = read_ints(R, f"Enter available resources of each type ({R} types): ")
    print(f"Enter Maximum matrix ({P} processes x {R} resources):")
    for i in range(P):
        maximum[i] = read_ints(R)
    print("Enter Allocation matrix:")
    for i in range(P):
        allocation[i] = read_ints(R)
    calculate_need()
    safe, safe_seq = is_safe()
    if safe:
        print("System is in a SAFE state.\nSafe sequence: ", end="")
        for i in range(P):
            print(f"P{safe_seq[i]} ", end="")
        print()
    else:
        print("System is in an UNSAFE state.")
    pid = read_ints(1, "\nEnter process number requesting resources: ")[0]
    request = read_ints(R, f"Enter request vector ({R} values): ")
    request_resources(pid, request)
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 bankers.py
```
## Sample Output
```
Enter available resources of each type (3 types): 3 3 2
Enter Maximum matrix (5 processes x 3 resources):
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3
Enter Allocation matrix:
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
System is in a SAFE state.
Safe sequence: P1 P3 P4 P0 P2
Enter process number requesting resources: 1
Enter request vector (3 values): 1 0 2
Request can be granted safely.
```