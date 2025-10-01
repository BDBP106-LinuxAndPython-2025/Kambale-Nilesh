#2 Write a script to convert the decimal number D into binary.
x=int(input("Enter the number: "))
s=str("")
while x >0:
    remainder=x%2
    s=str(remainder)+s
    x=x//2
print(f'The binary of {x} is : ({s})')
