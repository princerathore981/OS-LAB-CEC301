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
