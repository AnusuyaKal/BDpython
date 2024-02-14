class CustomFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Example usage
with CustomFileHandler('example.txt', 'w') as file:
    file.write('Hello, world!')

# Example usage
#with open('example.txt', 'w') as file:
#    file.write('Hello, World!')

