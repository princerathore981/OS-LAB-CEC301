# Program 8
### Contiguous Memory Allocation — First Fit, Best Fit and Worst Fit
## Aim
To implement First Fit, Best Fit and Worst Fit memory allocation strategies for
contiguous memory partitioning and compare their block allocation and fragmentation.
## Theory
- In contiguous memory allocation, each process is allocated a single contiguous block
of memory from a list of free memory blocks (holes).
- First Fit allocates the first hole that is big enough — fast, but can leave many small
unusable fragments at the start of memory.
- Best Fit allocates the smallest hole that is big enough — minimizes leftover space
per allocation but leaves many tiny unusable fragments over time and is slower
(searches the entire list).
- Worst Fit allocates the largest available hole — leaves the largest possible leftover
fragment, which may remain usable for future requests.
## Program (Python)
```
MAX = 20
def first_fit(bsize, bn, psize, pn):
    block = bsize[:bn]
    allocation = [-1] * pn
    for i in range(pn):
        for j in range(bn):
            if block[j] >= psize[i]:
                allocation[i] = j
                block[j] -= psize[i]
                break
    print("\n--- First Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        print(f"P{i + 1}\t\t{psize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"B{allocation[i] + 1}")
        else:
            print("Not Allocated")
def best_fit(bsize, bn, psize, pn):
    block = bsize[:bn]
    allocation = [-1] * pn
    for i in range(pn):
        best_idx = -1
        for j in range(bn):
            if block[j] >= psize[i]:
                if best_idx == -1 or block[j] < block[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            block[best_idx] -= psize[i]
    print("\n--- Best Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        print(f"P{i + 1}\t\t{psize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"B{allocation[i] + 1}")
        else:
            print("Not Allocated")
def worst_fit(bsize, bn, psize, pn):
    block = bsize[:bn]
    allocation = [-1] * pn
    for i in range(pn):
        worst_idx = -1
        for j in range(bn):
            if block[j] >= psize[i]:
                if worst_idx == -1 or block[j] > block[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            block[worst_idx] -= psize[i]
    print("\n--- Worst Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        print(f"P{i + 1}\t\t{psize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"B{allocation[i] + 1}")
        else:
            print("Not Allocated")
def main():
    bn = int(input("Enter number of memory blocks: "))
    bsize = list(map(int, input("Enter sizes of blocks: ").split()))[:bn]
    pn = int(input("Enter number of processes: "))
    psize = list(map(int, input("Enter sizes of processes: ").split()))[:pn]
    first_fit(bsize, bn, psize, pn)
    best_fit(bsize, bn, psize, pn)
    worst_fit(bsize, bn, psize, pn)
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 memory_allocation.py
```
## Sample Output
```
Enter number of memory blocks: 5
Enter sizes of blocks: 100 500 200 300 600
Enter number of processes: 4
Enter sizes of processes: 212 417 112 426--- First Fit --
Process No.     Process Size    Block No.
P1      212     B2
P2      417     B5
P3      112     B2
P4      426     Not Allocated--- Best Fit --
Process No.     Process Size    Block No.
P1      212     B4
P2      417     B2
P3      112     B3
P4      426     B5
--- Worst Fit ---
Process No.     Process Size    Block No.
P1      212     B5
P2      417     B2
P3      112     B5
P4      426     Not Allocated
```