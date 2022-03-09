from threading import Thread
from time import sleep, perf_counter


def task():
    print('Starting a task ...')
    sleep(1)
    print('Done')
    
start_time = perf_counter()

# Create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

# Notes: 
# When the program excutes, it'll have three threads: 
# the main thread is created by the Python interpreter, 
# and two new threads are created by the program
print(f"It took {end_time - start_time: 1.2f} seconds(s) to complete.")
