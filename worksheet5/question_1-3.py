#(1) Explain the various ways of importing module contents with examples
# i)   import fact   if fact present in present directory then we can call  as import fact.py
# ii)  from fact import factorial // calling function fron module
# iii) import fact as f // then we can call fumction as f.factorial()
# iv)  another way fact.fcatorial()
# v)   first import pkg1 then from pkg1 import module1,


# (2) How does Python know where to search for modules and packages?
#   i)  when we import module python will check in current directory first then it will search in
#      Directories listed in environment variable as path
#      then it will search in standard library directories
#      then it will search in third-party directory
#   ii) in case user created package if import happen in current directory then it will search & import the directory
#      else need to explictly mention path in need to import. the directory must have __init__.py

# (3)  How are packages different from modules? How are modules different from functions?
#     And how are methods different from functions?
#   i)   module belong to package , function belong to module , method belong to class or function
#   ii)  Thus analogy becomes package → module → function → method
#   iii) package----A directory (folder) containing one or more modules and an __init__.py file.
#   iv)  module-----A single Python file that can contain functions, classes, and variables.
#   v)   function---A block of reusable code inside a module (or class) that performs a specific task
#   vi)  method-----Defined inside a class and Called on an object (instance)
