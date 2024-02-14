import pdb

def inner():
    x = 1
    y = 2
    pdb.set_trace()
    z = 3
    return z

def outer():
    a = 10
    b = 20
    result = inner()
    c = 30
    return result

outer()
