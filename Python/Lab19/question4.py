# (4) Write a program to filter out the odd elements of the Fibonacci series for the first n
# terms.
n=int(input("Enter the value of n:"))
f1=0
f2=1
list_of_fibonacci = [0]
for i in range(n):
    f3=f1+f2
    f1=f2
    f2=f3
    list_of_fibonacci.append(f2)
print(list_of_fibonacci)
def odd(x): return x%2!=0
filteredOut_series=filter(odd,list_of_fibonacci)
print(list(filteredOut_series))
