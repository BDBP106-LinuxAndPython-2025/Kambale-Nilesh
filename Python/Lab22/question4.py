# (4) Write a decorator called @track_calls that counts how many times a function has been
# called. It also should print the function name and the number of calls each times it is
# executed. Instead of printing the output to the screen, log the output in a file.
def track_call(func):
    func.count=0
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func.count+=1

        call_f=f' function {func.__name__} was called {func.count} Times'

        f=open("function_called.txt","w")
        f.write(call_f)
        f.close()
        return func(*args, **kwargs)
    return wrapper


    return wrapper
@track_call
def fahrenheite(c):
    return (c * 9/5) + 32

fahrenheite(74)
fahrenheite(37)
fahrenheite(121)
fahrenheite(63)
fahrenheite(92)