# 3)Write a program to find the maximum and minimum values of a dictionary.
D=dict(a=1,b=2,c=3,d=44,g=7,h=8)
mi=D['a']
ma=D['a']
for key,value in D.items():
    if mi >= value:
        mi=value
    if ma <= value:
        ma=value
print(f'maximum value of dictionary is {ma} & minimun is {mi}')

 #min_value = min(D.values())                    // optional code
 #max_value = max(D.values())
 #print(min_value, max_value)