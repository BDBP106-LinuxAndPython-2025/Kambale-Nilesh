#4)Given a dictionary with a values list, extract the key whose value has the most unique
# values.
test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
for key,value in test_dict.items():
    count=0
    for i in set(value):
        count+=1

    test_dict[key]=count

#print(test_dict)
MK=max(test_dict,key=test_dict.get)
print(f'The key whose value has the most unique value is: {MK}')
