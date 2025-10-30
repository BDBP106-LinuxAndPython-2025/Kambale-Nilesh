"""(10) Write a decorator measure_time to calculate how long a function takes to run. Use it
 on the above function calculating population growth that loops 1 million iterations."""
def measure_time(func):
    def wrapper_func():
        t=__import__('time')
        start_time=t.perf_counter()
        func()
        end_time=t.perf_counter()
        print("Time Taken:",end_time - start_time ,"seconds")
    return wrapper_func

import math
def population_growth():
    N0=10
    r=0.2
    t=2
    def exponential_growth(N0,r,t):
        e=math.e
        return N0 * e**(r * t)
    for i in range(1000000):
        Nt=round(exponential_growth(N0,r,t))
    print (f"Population after {t} years: {Nt}")

@measure_time
def run_population_growth():
    population_growth()

run_population_growth()