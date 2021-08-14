import threading
import queue
import time

shutdown_event = threading.Event()
q = queue.Queue()


def counter(amount):
    x = range(amount)
    for y in x:
        print(y)


def worker():
    while not shutdown_event.is_set():
        try:
            item = q.get(block=True, timeout=0.05)
            counter(item)
            q.task_done()
        except queue.Empty:
            continue


def main():
    # print('Hello')
    num_worker_threads = 3
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()

    for i in range(7):
        q.put(1)

    q.join()
    print(f"Threads: {threading.active_count()}")
    shutdown_event.set()
    time.sleep(0.5)
    print(f"Threads: {threading.active_count()}")


if __name__ == '__main__':
    main()
