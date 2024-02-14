from contextlib import contextmanager

@contextmanager
def file_open(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

# Example usage
with file_open('example.txt', 'w') as f:
    f.write('Hello, world!')
