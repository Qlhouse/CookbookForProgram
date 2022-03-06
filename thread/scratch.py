from threading import Thread
import threading
import time


def my_function():
    # print(f"printing from thread, is running {my_function.__hash__}")
    print(threading.currentThread().getName(), ' Starting', sep="...")
    time.sleep(2)
    print(threading.currentThread().getName(), ' Exiting', sep="...")


if __name__ == "__main__":
    threads = [Thread(target=my_function) for _ in range(10)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
