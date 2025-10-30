#!/usr/bin/python3

"""Write a function population_growth(initial,rate, time) that definss an inner func-
tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
represents the initial population and N(t) is population after time t. The inner function
returns the population after time, and the outer function rounds and prints it."""

import math


def population_growth(initial, rate, time):
    def exponential_growth():
        result =  initial + math.exp(rate * time)
        return result

    population = exponential_growth()
    print(round(population))

initial=int(input("Enter the initial population: "))
rate=int(input("Enter the rate of growth: "))
time=int(input("Enter the time: "))
population_growth(initial, rate, time)
