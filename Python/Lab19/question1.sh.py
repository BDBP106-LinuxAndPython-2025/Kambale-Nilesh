#(1) Write a program to convert temperature in Celsius to Fahrenheit using map function.
#x=int(input("Enter the value of temperatue in degree celsius: "))

# def fahrenheit(x):return x+32
# print(x)
# result=(lambda x:x*9/5, x )
def fahrenheit(x): return (x*9)/5 + 32
a = list(map(int, input("Enter the temperature in celsius: ").split()))
result=list(map(fahrenheit,a))
print("The temperature in fahrenheit is: ", result)

# result=list(map(lambda x:(x*9/5)+32 , a))
# print("The temperature in celsius is: ", result)
# result=list(map(lambda x:1.8*x+32 , a))
# print("The temperature in celsius is: ", result)