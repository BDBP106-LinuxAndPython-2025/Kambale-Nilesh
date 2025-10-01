# 1) Write a script to find the sum of squares of frist N numbers
x=input("Enter sequence of numbers: ")
z=int(input("Enter the value of N : "))
L=[]
for i in x: #storing square of given sequence
    y=int(i)
    y*=y
    L.append(y)
print(f'The list of square of given sequence: {L}')
sum=0
for i in L[:z:1]: # storing sum of square
    sum+=i
print(f'The sum of square of given sequence till ({z}) term : {sum}')









