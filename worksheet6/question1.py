# 1) Define a class called ’Car’. The class intance should take required arguments as make,
# model, year and color. Define default values of ’False’ for the attributes called ’started’,
# 0 for the attribute ’speed’, and ’200’ as the maximum speed. There should be a total of
# 7 attributes in the __init__ function.
# (a) Create an instance of the above class called toyota_camry with arguments of car
# make as ’Toyota’, model as ’Camry’, year as ’2022’ and color ’Red’. Print the values of
# these attributes using the instance you just created.
# (b) Create another instance of this class called ’ford mustang’ with make as ”Ford”,
# model as ”Mustang”, year 2022 and color ’Black’.Print all the 7 attributes for this in-
# stance.
# (c) How can you be sure that the above attributes belong to the instance and not the
# class? Try typing print(Car.make). Do you get an error, and if so what error do you
# get? How will you fix this error in your main program?
# (d) Execute the command print(Car.__dict__). Describe the output. The __dict__
# attribute holds a dictionary containing the writable members of the underlying class or
# instance. Each key value represents an attribute or method name. When you access a
# class member through the class object, Python automatically searches for the member’s
# name in the __dict. If the name isn’t there, you get an AttributeError.
# (e) Now define a class attribute called showroom with value NewAge. Also define a func-
# tion with decorator @classmethod that changes this value upon user request. Again
# print the value of __dict__ attribute, what is the output? Describe the output.
# (f) Print the value of toyota_camry.__dict__. How is this output different from
# Car.__dict__? Explain.
# (g) Python also supports what are called magic methods or dunder (double underscore)
# methods that are called automatically in response to specific operations. For example, de-
# fine a function as below. and execute the statement print(str(<name-of_class)). Test
# this with the above two class instances you created. For example str(toyota_camry).
# What is the output? There are other magic methods such as ___iter__, __repr__ etc.
# (h) Define a static method called show_intro_message that prints the purpose of this
# class.
# def __str__(self):
# return f"{self.make} {self.model} {self.color| ({self.year})"

class Car:

    def __init__(self, make, model, year, color, started=False, speed=0, max_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color = color   # 7 attributes
        self.started = started
        self.speed = speed
        self.max_speed = max_speed

    showroom = "NewAge"

    # (e)
    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name

    # (g)
    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.color} | Showroom: {self.showroom}"

    # (h)
    @staticmethod
    def show_intro_message():
        print("This represnts attributes & object (car).")


# (a)
toyota_camry = Car("Toyota", "Camry", 2022, "Red")
print("Toyota Camry attributes:")
print(toyota_camry.make, toyota_camry.model, toyota_camry.year, toyota_camry.color)

# (b)
ford_mustang = Car("Ford", "Mustang", 2022, "Black")
print("Ford Mustang attributes:")
print(ford_mustang.make, ford_mustang.model, ford_mustang.year, ford_mustang.color)

# (c)
try:
    print(Car.make) #print("\n(c) Checking instance vs class attributes:"
except AttributeError as e:
    print("Error:", e)

print("Accessing instance attribute :", ford_mustang.make)

# (d)
print("\n(d) Car.__dict__ output:")
print(Car.__dict__)

# (e)
print("\nBefore changing :", Car.showroom)
Car.change_showroom("Future Motors")
print("After changing :", Car.showroom)
print("Updated Car.__dict__:")
print(Car.__dict__)

# (f)
print("\n(f) toyota_camry.__dict__:")
print(toyota_camry.__dict__)

# Difference: Car.__dict__ holds class-level info (methods, attributes, etc.), while toyota_camry.__dict__ holds only instance attributes.

# (g)
print("\n(g) String representation with help of __str__:")
print(str(toyota_camry))
print(str(ford_mustang))

# (h)
print("\n(h) Static method :")
Car.show_intro_message()