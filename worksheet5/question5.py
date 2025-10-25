# (5) Define a module called prime that contains a function isPrime() that returns whether
# the passed argument is prime or not. Using this module and function, write another
# program containing a function printPrimes() that prints the first n prime numbers.
from prime import isprime
n=int(input("Enter term till you want to check prime number: "))
def check_prime(n):
    L=[]
    for i in range(2, n+1):
        if isprime(i):
            L.append(i)

    return L

result=check_prime(n)
print(result)
