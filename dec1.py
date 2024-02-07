def dollar(func):
    def wrapper():
        print("$$$$$")
        func()
        print("eeeee")
    return wrapper