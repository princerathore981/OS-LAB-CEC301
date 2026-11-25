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
