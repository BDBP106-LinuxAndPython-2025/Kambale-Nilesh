x=int(input("Enter the base: "))
n=int(input("Enter the power "))
y=x
for i in range(n-1):
      x=x*y
print(f'The {y} to the power {n} is {x} ')
