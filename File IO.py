
# Writing to a file using a context manager


with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# Reading from a file using a context manager
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
