import time
import requests
from threading import Thread
from queue import Queue
from queue import Empty

SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
THREAD_POOL_SIZE = 4

# [TODO] Refactory the codes to three classes, clarify each one


def fetch_rates(base):
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]

    # Note: same currency exchanges to itself 1:1
    rates[base] = 1.

    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


# Single thread mode
def main():
    for base in BASES:
        fetch_rates(base)


def main_thread_implementation():
    threads = []
    for base in BASES:
        thread = Thread(target=fetch_rates, args=[base])
        thread.start()
        threads.append(thread)

    while threads:
        threads.pop().join()


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()  # Obtain a new item in a non-blocking fashion
        except Empty:
            break
        else:
            fetch_rates(item)
            work_queue.task_done()  # Mark the item as processed


def main_thread_pool_implementation():
    work_queue = Queue()

    for base in BASES:
        work_queue.put(base)

    threads = [Thread(target=worker, args=(work_queue,))
               for _ in range(THREAD_POOL_SIZE)]

    for thread in threads:
        thread.start()

    work_queue.join()   # Wait until all items have been processed

    while threads:
        threads.pop().join()    # Wait for all threads to finish


if __name__ == "__main__":
    started = time.time()
    # main()
    # main_thread_implementation()
    main_thread_pool_implementation()
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))
