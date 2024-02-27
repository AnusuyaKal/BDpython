
# # # # Writing to a file using a context manager


# with open('example.txt', 'w') as file:
#     file.write('Hello, world!')

# # Reading from a file using a context manager
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# import sqlite3

# # Define a function to create a context manager for database connections
# class DatabaseConnection:
#     def __init__(self, database):
#         self.database = database

#     def __enter__(self):
#         self.connection = sqlite3.connect(self.database)
#         print("enter")
#         return self.connection
        

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.connection:
#             self.connection.close()
#             print("exit")

# # Example usage
# database_file = 'example.db'

# # Using the context manager to establish a database connection
# with DatabaseConnection(database_file) as connection:
#     cursor = connection.cursor()

#     # Execute SQL queries or perform database operations
#     print("with")
#     cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
#     cursor.execute('INSERT INTO users (name) VALUES (?)', ('John',))
#     cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))

#     # Commit the changes
#     connection.commit()

# The database connection is automatically closed when exiting the 'with' block


import threading

# Define a lock
lock = threading.Lock() #synchronize access to shared resources

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




# # from contextlib import contextmanager

# # @contextmanager
# # def file_manager(filename, mode):
# #     try:
# #         # Resource allocation (opening the file)
# #         file = open(filename, mode)
# #         print(f"File '{filename}' opened in mode '{mode}'")
# #         yield file  # yields control back to the caller, allowing code inside the with block to run.

# #     finally:
# #         # Resource deallocation (closing the file)
# #         if file and not file.closed:
# #             file.close()
# #             print(f"File '{filename}' closed")

# # # Example usage
# # with file_manager('example.txt', 'w') as file:
# #     print("inside the with statement")
# #     file.write('Hello, world!\n')
