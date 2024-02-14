import pdb

def some_function():
    x = 5
    pdb.set_trace()  # Set a breakpoint here
    y = 10
    result = x + y
    return result

print(some_function())
