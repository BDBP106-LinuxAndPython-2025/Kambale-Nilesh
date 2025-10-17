# (4) Write a Python function checkList that accepts a list and an index, and prints the
# element of the list at the index position. Catch the IndexError and TypeError and
# display appropriate messages. Call the function for (a) number list and index, (b) A
# string input and index, (c) A boolean value (True) and index and (d) A string input and
# incorrect index.

def checklist(list,index):
    try :
        print(f'Element at index {index} is: {list[index]}')
    except IndexError:
        print("Give valid index")
    except TypeError:
        print("Enter a valid list or index ")

print("(a) number list and index")
checklist([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],0)

print("\n(b) A string input and index")
checklist("BDBH101",0)

print("\n(c) A boolean input and index")
checklist(True,1)

print("\n(d) A string input and index")
checklist("BDBH101",15)
