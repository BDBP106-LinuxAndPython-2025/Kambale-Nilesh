# (2) Create a decorator to measure the execution time of a function. Please demonstrate
# using a sample function (add sleep for checking) and a decorator for this sample function
# that measures the execution time.
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}Execution time: {end - start,}')
    return wrapper
@execution_time
def fahrenheit(c):
    time.sleep(3)
    return (c * 9/5) + 32

fahrenheit(5)




