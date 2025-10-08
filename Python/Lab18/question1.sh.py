#(i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.

b=[i+1 for i in range(50)] #FRIST METHOD RANGE BECOMES i+1 T0 50 so i=0 thus 0+1=1 so 1 To 50
print(b)
a=[i for i in range(1,51)] #HERE THE i=1 TO (len-1) THUS 51-1 SO TILL 50 IT WILL PRINT TILL 50
print(a)
# (ii) Slicing with positive step:
print(a[1:5]) # a) start=2 stop=5 step=1, start > stop here it print from index 1 to 4 thus list starts from 0 index it contain 1

print(f'result={a[3:20:2]} value of start=4 stop=20 & step=2 it will print all even numbers')

print(f'result={a[::2]} value of start=1 stop=50 & step=2 thus no start & stop index given it will asume deafult 0 To len-1 so it will print all odd values  ')

print(f'result={a[::]} value of start=1 stop=50 & step=1 it will print all numbers asumming deafult values in step of 1')

print(f'result={a[10::2]} value of start=11 stop=49 & step=2 so no stop index is given it assume last index as stop & in step of 2 it will print all odd number from 11 to 50')

print(f'result={a[1:1:]} value of start=null stop=null & step=1 thus start & stop value is same it will be empty list')

print(f'result={a[:0:]} value of start=1 stop=1 & step=1 So start index i not given it will be deaful 0 & stop index is 0 so it will be Empty list ')

print(f'result={a[-7::1]} value of start=44 stop=50 & step=1 so index starts from is -7 which is 43 index (len-7)')

print(f'result={a[-6:]} value of start=45 stop=50 & step=1 so start index is -6 index (len-6) which is index 44 which has value 45 thus ')

print(f'result={a[-10:-4:]} value of start=41 stop=46 & step=1 so start index is len-10 is 40 has value 41 & stop index is len-1(50-4)=46 & it will exclude last index thus 45 which has value 46')

#(iii) Slicing with negative step:
print(f'result={a[::-1]} value of start=50 stop=1 & step=-1 so steps are in reverse -1 order it start from len-1 index to 0 which is 50-1=49 which has value 50 & thus at every itration it will -1 index & thus value  ')

print(f'result={a[::-3]} value of start=50 stop=2 & step=-3 it start from len-1 to 0 index which is 49 to 0 in step of -3 thus ti will print index 49 value 50 & 46 has value 47 ')

print(f'result={a[:1:-2]} value of start=50 stop=2 & step=-2 it start from len-1 to 1 index in step of -2 thus index 49,47,....3 which has value 50,48...4 it will exclude last index by step involved ')

print(f'result={a[-1:-1:-1]} value of start=50 stop=50 & step=-1 thus start & stop index is same it will print empty list ')

print(f'result={a[-5:-1:1]} value of start=46 stop=50 & step=1 for here index will be len-5 = 45 has value of 46 len-1 49 has 50 & it wil be exclude last index49 thus 48 stop thus in step of 1 [46,47,48,49,]')

print(f'result={a[:-5:-1]} value of start=50 stop=47 & step=-1 so -1 step it will start from len-1 to len-5  which mean 49 to 45 index thus it will not consider the last index thus till 46 it has value 47 ')

print(f'result={a[-1:5:-1]} value of start=50 stop=7 & step=-1 it will print len-1 to 5 index so it will skip one index thus 6th which has value 7 [50,49..7]')

print(f'result={a[2:2:-1]} value of start=3 stop=3 & step=-1 thus start & stop value is same it will be empty list  []')

print(f'result={a[2:1:-1]} value of start=3 stop=2 & step=-1 it -1 step it will len-1 start index 2 which has value 3  & 2 has value 1 [3] ')

print(f'result={a[0:-5:]} value of start=1 stop=45 & step=1 so start index is 0 and end is -5 so (len-5)-1) 44 index print till 45 ')

# (iv) Modification of lists using list slicing:
#       (a) Create a list of even numbers from a using list slicing technique.
print(a[1::2])
#       (b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.
print(a[:10:])
print(a[35::2])
