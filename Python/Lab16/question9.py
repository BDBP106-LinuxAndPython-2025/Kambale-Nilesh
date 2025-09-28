x=input("Enter the first string: ")
y=input("Enter the second string: ")
c=0
for i in x:
    for j in y:
        if i==j:
            c+=1


if len(x)==c & len(y)==c:
    print(f'The string {x} and {y} are anagrams')
else:
    print(f'The string {x} and {y} are not anagrams')

