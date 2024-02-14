from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        # Resource allocation (opening the file)
        file = open(filename, mode)
        print(f"File '{filename}' opened in mode '{mode}'")
        yield file  # This allows the caller to use the file within the context

    finally:
        # Resource deallocation (closing the file)
        if file and not file.closed:
            file.close()
            print(f"File '{filename}' closed")

# Example usage
with file_manager('example.txt', 'w') as file:
    file.write('Hello, world!\n')
