def magic_date():
    x=int(input("Enter the date:"))
    z=int(input("Enter the month:"))
    y=int(input("Enter the year:"))
    if (x * z) == (y % 100):
        print("Given date is magical date.")
    else:
        print("Given date is not magical date.")
magic_date()


#function without the user input
def magic_date(x,z,y):
    if (x * z) == (y % 100):
        return True
    else:
        return False

#main program
for y in range(1900,2000):
    for z in range(1,13):
        for x in range(1,32):
            if magic_date(x,z,y)==True:
                print(f'{x}/{z}/{y}')