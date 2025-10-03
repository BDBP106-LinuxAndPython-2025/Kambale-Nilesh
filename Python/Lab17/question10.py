# (10) Write a function called nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter.
# The main program should read an integer from the user and display the first prime
# number larger than the entered value.
x=int(input("Enter the integer: "))
def nextprime(num):
    a=num+1
    while True:
        isprime=True
        for i in range(2,a):
            if a%i==0:
                isprime=False
                break
        if isprime:
            break
        a+=1
    print(a)
nextprime(x)
