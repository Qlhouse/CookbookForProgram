from threading import Thread
from time import sleep, perf_counter
import os
import time

def replace(filename, substr, new_substr):
    # print(f"Processing the file {filename}")
    # Get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # Replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # Write data into the file
    with open(filename, 'w') as f:
        f.write(content)

def create_files():
    os.makedirs('c:/temp/', exist_ok=True)
    for i in range(1, 51):
        filename = os.path.join('c:/temp/', f"test{i}.txt")
        with open(filename, 'w') as f:
            f.write("Create a new text file!")

def main_single_thread():
    filenames = os.scandir('c:/temp/')
    for filename in filenames:
        replace(filename, 'new', 'replaced')

def main_multiple_thread():
    filenames = os.scandir('c:/temp/')

    # Create threads
    threads = [Thread(target=replace, args=(filename, 'new', 'replaced'))
            for filename in filenames]
    
    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to complete
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    create_files() 
    start_time = perf_counter()
    main_single_thread()
    end_time = perf_counter()
    print(f"It took {end_time - start_time: 0.2f} seconds(s) to complete in single thread.")

    time.sleep(2)

    create_files() 
    start_time = perf_counter()
    main_single_thread()
    end_time = perf_counter() 
    print(f"It took {end_time - start_time: 0.2f} seconds(s) to complete in multiple thread.")
