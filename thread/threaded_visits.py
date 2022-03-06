from threading import Thread
from threading import Lock
import time

thread_visits = 0
thread_visits_lock = Lock()


def visit_counter():
    global thread_visits
    for i in range(100_000):
        value = thread_visits
        thread_visits = value + 1  # [TODO] The difference thread_visits += 1


def visit_counter_with_lock():
    global thread_visits
    for i in range(100_000):
        with thread_visits_lock:
            thread_visits += 1


if __name__ == "__main__":
    start_time = time.time()
    thread_count = 1000
    # threads = [Thread(target=visit_counter) for _ in range(thread_count)]
    threads = [Thread(target=visit_counter_with_lock)
               for _ in range(thread_count)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("---- %s seconds ----" % (time.time() - start_time))
    # print(f"thread_count={thread_count}, thread_visits={thread_visits}")
    print(f"{thread_count=}, {thread_visits=}")
