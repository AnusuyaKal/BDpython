import pdb

def add(a, b):
    # Debugger will stop here
    result = a + b
    pdb.set_trace()  # Debugger will stop here
    return result

def subtract(a, b):
    # Debugger will stop here
    result = a - b
    return result

def multiply(a, b):
    # Debugger will stop here
    result = a * b
    return result

def divide(a, b):
    # Debugger will stop here
    result = a / b
    return result

def main():
    # Debugger will stop here
    x = 10
    y = 5
    z = add(x, y)
    z = subtract(z, y)
    z = multiply(z, y)
    z = divide(z, y)
    print("Result:", z)

if __name__ == "__main__":
    pdb.run("main()")
