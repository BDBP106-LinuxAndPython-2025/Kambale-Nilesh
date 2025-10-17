# (3) Child class and user-defined error Define a custom error class called AgeTooYoungError
# that extends Exceptions. In a function called checkAge that takes age as input, if the
# age is less than 18, raise the AgeTooYoungError with the message (”Age must be more
# than 18”). In the except block, print the error message thrown in the try block. Call
# the function checkAge with 3 as the input.
class AgeToYoungError(Exception):
    def __init__(self,age):
        self.age=age
    def checkAge(self):

        if self.age>18:
            print("You are a adult person")
        else:
            print("You are a minor")
try:
    age= int(input())
    if age<18: raise AgeToYoungError(age)
except TypeError:
    print("You Entered a string value please enter a valid age")
except ValueError:
    print("You Entered a string value please enter a valid age")

finally:
    print()



