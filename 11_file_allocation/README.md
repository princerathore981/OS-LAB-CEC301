# Program 11
### File Allocation Methods — Contiguous, Linked and Indexed Allocation
## Aim
To simulate Contiguous, Linked and Indexed file allocation methods used by the
operating system to allocate disk blocks to files, and to display the block allocation
table for each.
## Theory
- Contiguous allocation stores each file as a set of contiguous blocks on the disk. It
gives excellent sequential and direct access performance but suffers from external
fragmentation and requires knowing the file size in advance.
- Linked allocation stores each file as a linked list of disk blocks scattered anywhere on
disk; each block contains a pointer to the next block. It eliminates external
fragmentation but only supports efficient sequential access, and pointers consume
space and are vulnerable to corruption.
- Indexed allocation brings all block pointers of a file together into one index block.
This supports efficient direct access and avoids external fragmentation, at the cost
of extra space for the index block.
## Program (Python)
```
MAXBLOCKS = 30
MAXFILES = 10
disk = [0] * MAXBLOCKS  # 0 = free, 1 = allocated
def reset_disk():
    for i in range(MAXBLOCKS):
        disk[i] = 0
def contiguous_allocation():
    reset_disk()
    print("\n--- Contiguous Allocation ---")
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        start, length = map(int, input(
            f"File {f + 1} - starting block, length: ").split())
        ok = 1
        for i in range(start, start + length):
            if i >= MAXBLOCKS or disk[i] == 1:
                ok = 0
                break
        if not ok:
            print("Allocation failed: blocks not free/out of range.")
            continue
        for i in range(start, start + length):
            disk[i] = 1
        print(f"File {f + 1} allocated blocks {start} to {start + length - 1}")
def linked_allocation():
    reset_disk()
    print("\n--- Linked Allocation ---")
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        length = int(input(f"File {f + 1} - number of blocks: "))
        print(f"File {f + 1} allocated blocks: ", end="")
        prev = -1
        count = 0
        i = 0
        while i < MAXBLOCKS and count < length:
            if disk[i] == 0:
                disk[i] = 1
                print(f"{i} ", end="")
                if prev != -1:
                    print("-> ", end="")
                prev = i
                count += 1
            i += 1
        print("(NULL)")
        if count < length:
            print("Warning: disk full, could not allocate all blocks.")
def indexed_allocation():
    reset_disk()
    print("\n--- Indexed Allocation ---")
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        length = int(input(f"File {f + 1} - number of data blocks needed: "))
        index_block = -1
        for i in range(MAXBLOCKS):
            if disk[i] == 0:
                index_block = i
                disk[i] = 1
                break
        print(f"File {f + 1} - Index block: {index_block}, Data blocks: ", end="")
        count = 0
        i = 0
        while i < MAXBLOCKS and count < length:
            if disk[i] == 0:
                disk[i] = 1
                print(f"{i} ", end="")
                count += 1
            i += 1
        print()
def main():
    print("Menu:\n1. Contiguous Allocation\n2. Linked Allocation")
    print("3. Indexed Allocation")
    choice = int(input("Enter choice: "))
    if choice == 1:
        contiguous_allocation()
    elif choice == 2:
        linked_allocation()
    elif choice == 3:
        indexed_allocation()
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
```
## Compilation & Execution
```
python3 file_allocation.py
```
## Sample Output
```
Menu:
1. Contiguous Allocation
2. Linked Allocation
3. Indexed Allocation
Enter choice: 3--- Indexed Allocation --
Enter number of files: 2
File 1 - number of data blocks needed: 4
File 1 - Index block: 0, Data blocks: 1 2 3 4 
File 2 - number of data blocks needed: 3
File 2 - Index block: 5, Data blocks: 6 7 8
```