#(2) Write the above program using lambda expression.
def fahrenheit(x):return x
a = list(map(int, input("Enter the temperature in celsius: ").split()))
result=list(map(lambda x:(x*9/5)+32 , a))
print("The temperature in celsius is: ", result)