import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@measure_time
def my_function(n):
    # Simulate some computation
    time.sleep(1)
    return n * n

result = my_function(5)
print("Result:", result)
