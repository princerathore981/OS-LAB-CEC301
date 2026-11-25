# Program 9
### Page Replacement Algorithms — FIFO, LRU and Optimal
## Aim
To implement and compare the FIFO, Least Recently Used (LRU) and Optimal page
replacement algorithms used in demand paging, and to count the number of page
faults produced by each for a given reference string.
## Theory
- In demand paging, when a referenced page is not in memory (a page fault) and all
frames are full, the OS must select a victim page to replace, based on a
page-replacement algorithm.
- FIFO replaces the page that has been in memory the longest, regardless of usage —
simple but can suffer from Belady's Anomaly (more frames causing more faults).
- LRU replaces the page that has not been used for the longest period of time —
approximates optimal behaviour based on the principle of locality of reference.
- The Optimal (MIN) algorithm replaces the page that will not be used for the longest
time in the future — it gives the theoretical minimum number of page faults but
requires future knowledge and is used only as a benchmark.
## Program (Python)
```
MAXFRAMES = 10
MAXPAGES = 50
def is_present(frames, nf, page):
    for i in range(nf):
        if frames[i] == page:
            return 1
    return 0
def fifo(ref, n, nf):
    frames = [-1] * nf
    front = 0
    faults = 0
    for i in range(n):
        if not is_present(frames, nf, ref[i]):
            frames[front] = ref[i]
            front = (front + 1) % nf
            faults += 1
    print(f"FIFO Page Faults = {faults}")
def lru(ref, n, nf):
    frames = [-1] * nf
    last_used = [0] * nf
    filled = 0
    faults = 0
    for i in range(n):
        pos = -1
        for j in range(nf):
            if frames[j] == ref[i]:
                pos = j
                break
        if pos == -1:
            faults += 1
            if filled < nf:
                frames[filled] = ref[i]
                last_used[filled] = i
                filled += 1
            else:
                # find least recently used frame
                lru_idx = 0
                for j in range(1, nf):
                    if last_used[j] < last_used[lru_idx]:
                        lru_idx = j
                frames[lru_idx] = ref[i]
                last_used[lru_idx] = i
        else:
            last_used[pos] = i
    print(f"LRU Page Faults = {faults}")
def optimal(ref, n, nf):
    frames = [-1] * nf
    filled = 0
    faults = 0
    for i in range(n):
        if is_present(frames, filled, ref[i]):
            continue
        faults += 1
        if filled < nf:
            frames[filled] = ref[i]
            filled += 1
            continue
        # find the frame whose page is used farthest in future (or never)
        replace_idx = -1
        farthest = -1
        for j in range(nf):
            k = i + 1
            while k < n:
                if frames[j] == ref[k]:
                    break
                k += 1
            if k == n:  # never used again
                replace_idx = j
                break
            if k > farthest:
                farthest = k
                replace_idx = j
        frames[replace_idx] = ref[i]
    print(f"Optimal Page Faults = {faults}")
def main():
    n = int(input("Enter number of pages in reference string: "))
    ref = list(map(int, input("Enter the reference string: ").split()))[:n]
    nf = int(input("Enter number of frames: "))
    fifo(ref, n, nf)
    lru(ref, n, nf)
    optimal(ref, n, nf)
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 page_replacement.py
```
## Sample Output
```
Enter number of pages in reference string: 12
Enter the reference string: 7 0 1 2 0 3 0 4 2 3 0 3
Enter number of frames: 3
FIFO Page Faults = 9
LRU Page Faults = 8
Optimal Page Faults = 7
```