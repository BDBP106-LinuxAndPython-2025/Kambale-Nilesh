# (8) In the above exercise, let’s use an in-built decorator function called lru_cache, where
# lru stands for least recently used – It caches/stores the results of function calls, so
# that if the same input occurs again, it reuses the stored result instead of recomputing it.
# Least recently used means that it keeps the most recent results and discards the oldest
# ones if the cache gets full. We have control over the size of this cache, An example usage
# is given below.
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def factorial(n):
# if n==0 or n==1: return 1
# if n>1: return n*factorial(n-1)
# (i) Use a similar setup for the Fibonacci series calculation with maxsize=5. What is
# the time difference you see with and without the use of lru_cache?
#
# (ii) Provide a docstring with ‘”This function outputs the sum of n Fibonacci num-
# bers”’ inside the function. Print fibonacci.__doc__ and observe the output.
#
# (iii) Use a custom decorator log_time to print the datetime.now() value at entry
# and exit for every func.__name__ call with the n (args) value
import time

from functools import lru_cache
import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} started at {time.time()} with args {args} and kwargs {kwargs}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} finished at {end} with result: {result}')
        print(f'Time taken by the function : {end - start:.6f}')
        return result
    return wrapper


@lru_cache(maxsize=5)
def fibonacci(n):
    """This function returns the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a


@time_taken
def fibo1(n):
    return fibonacci(n)


a = fibo1(10)
print("with lru cache", a)

fibonacci.cache_clear()


def fibonacci2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a


@time_taken
def fibo2(n):
    return fibonacci2(n)


a = fibo2(10)
print("without lru cache", a)

print(fibonacci.__doc__)





