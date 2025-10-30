# (12) Write a program to extract all vowels in a given string using list comprehension.
string1=input("Enter a string")
vowel=[i for i in string1.lower() if i=='a' or i=='e'or i=='o' or i=='i'or i=='u']
print(vowel)