import threading
import time
mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)
read_count = 0
shared_data = 0
def reader(id):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()  # first reader locks the resource
    mutex.release()
    print(f"Reader {id}: read shared_data = {shared_data}\n", end="")
    time.sleep(0.2)
    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()  # last reader unlocks the resource
    mutex.release()
def writer(id):
    global shared_data
    wrt.acquire()
    shared_data += 1
    print(f"Writer {id}: wrote shared_data = {shared_data}\n", end="")
    time.sleep(0.3)
    wrt.release()
def main():
    w = [None, None]
    r = [None] * 5
    w[0] = threading.Thread(target=writer, args=(1,))
    w[0].start()
    for i in range(5):
        r[i] = threading.Thread(target=reader, args=(i + 1,))
        r[i].start()
    w[1] = threading.Thread(target=writer, args=(2,))
    w[1].start()
    for i in range(5):
        r[i].join()
    w[0].join()
    w[1].join()
if __name__ == "__main__":
    main()
