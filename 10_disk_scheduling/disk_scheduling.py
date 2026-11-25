MAX = 50
def abs_diff(a, b):
    return a - b if a > b else b - a
def fcfs(req, n, head):
    total = 0
    cur = head
    for i in range(n):
        total += abs_diff(cur, req[i])
        cur = req[i]
    print(f"FCFS total head movement = {total}")
def sstf(req, n, head):
    visited = [0] * MAX
    total = 0
    cur = head
    for c in range(n):
        idx = -1
        best = 1 << 30
        for i in range(n):
            if not visited[i] and abs_diff(cur, req[i]) < best:
                best = abs_diff(cur, req[i])
                idx = i
        visited[idx] = 1
        total += best
        cur = req[idx]
    print(f"SSTF total head movement = {total}")
def scan(req, n, head, disk_size):
    arr = req[:n] + [head]
    arr.sort()
    idx = 0
    for i in range(n + 1):
        if arr[i] == head:
            idx = i
            break
    total = 0
    cur = head
    # go towards the higher end first
    for i in range(idx + 1, n + 1):
        total += abs_diff(cur, arr[i])
        cur = arr[i]
    total += abs_diff(cur, disk_size - 1)
    cur = disk_size - 1
    for i in range(idx - 1, -1, -1):
        total += abs_diff(cur, arr[i])
        cur = arr[i]
    print(f"SCAN total head movement = {total}")
def cscan(req, n, head, disk_size):
    arr = req[:n] + [head]
    arr.sort()
    idx = 0
    for i in range(n + 1):
        if arr[i] == head:
            idx = i
            break
    total = 0
    cur = head
    for i in range(idx + 1, n + 1):
        total += abs_diff(cur, arr[i])
        cur = arr[i]
    total += abs_diff(cur, disk_size - 1)  # go to the end
    total += (disk_size - 1)               # jump to 0 (cylinder 0)
    cur = 0
    for i in range(idx):
        total += abs_diff(cur, arr[i])
        cur = arr[i]
    print(f"C-SCAN total head movement = {total}")
def main():
    n = int(input("Enter number of requests: "))
    req = list(map(int, input("Enter the requests: ").split()))[:n]
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size (max cylinder + 1): "))
    fcfs(req, n, head)
    sstf(req, n, head)
    scan(req, n, head, disk_size)
    cscan(req, n, head, disk_size)
if __name__ == "__main__":
    main()
