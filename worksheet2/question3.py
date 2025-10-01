# Write a script that computes the number of 1s in a binary representation of a decimal
# number, N.
x=int(input("Enter the number: "))
s=str("")
while x >0:
    remainder=x%2
    s=str(remainder)+s
    x=x//2
print(f'The binary of {x} is : ({s})')
c=0
for i in s:
    if i=='1':
        c+=1
print(f'The Numbers of 1s in bin form is : {c} ')