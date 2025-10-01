#  Write a script to find the first occurrence of a character, c, in a string S.
x=input("Enter the string : ")
y=input("Enter the character c: ")
for i in range(len(x)):
    if x[i]==y:
        v=i+1
        break
print(f'the position of the occurance at {y} occured in string is: {v}')