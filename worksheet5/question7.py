# (7) Implement the Fibonacci function with parameter n. Call fibonacci(100) and use a
# decorator function to log the time taken to run this function.

import time
def timme_taken(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken by the function : {end - start:.6f}')
        return result
    return wrapper

@timme_taken
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        print(a)
a=fibonacci(100)
print(a)



