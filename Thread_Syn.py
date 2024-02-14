import threading

# Define a lock
lock = threading.Lock()

# Function to be executed by multiple threads
def thread_function():
    with lock:  # Acquire the lock using a context manager
        # Critical section
        # Access shared resources safely
        print("Thread {} is executing".format(threading.current_thread().name))

# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=thread_function)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
