import threading
NUM_THREADS = 4
def sum_array(p):
    """Thread function: p holds the argument (start, end) and the result (sum)."""
    p["sum"] = 0
    for i in range(p["start"], p["end"]):
        p["sum"] += i
    print(f"Thread {threading.get_ident() % 100000}: "
          f"sum[{p['start']}..{p['end']}) = {p['sum']}\n", end="")
def main():
    n = 1000000
    chunk = n // NUM_THREADS
    total = 0
    threads = []
    data = []
    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        data.append({"start": start, "end": end, "sum": 0})
        t = threading.Thread(target=sum_array, args=(data[i],))
        threads.append(t)
        t.start()
    for i in range(NUM_THREADS):
        threads[i].join()
        total += data[i]["sum"]
    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {total}")
if __name__ == "__main__":
    main()
