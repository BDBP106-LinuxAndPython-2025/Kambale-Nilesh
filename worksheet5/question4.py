# (4) Define a module called factorial that contains a function to find the factorial of a given
# integer. Using this function, find the permutation and combination of the given inputs.
import factorial
# dummy example in a group of 10 how many ways we can commity of 3 persons
# 10p3=           10!                               n!
#           = -------------   formula, p(n,r)==    ----
#               (10-3)!                           (n-r)!
n=int(input("Total no of item available: "))
r=int(input("Total number of item chosen : "))

def permutations(n,r):
    if n>r and r>0 and n>0:
        result=0
        result=factorial.factorial(n)/factorial.factorial(n-r)
        print(f'Permutations of {n} are {r}: ')
        return result
    else:
        raise ValueError("permutations cannot be called with n or r")

def combinations(n,r):
    if n>r and r>0 and n>0:
        result=0
        result=factorial.factorial(n)/(factorial.factorial(n-r))*factorial.factorial(r)
        print(f'Combinations of {n} are {r}: ')
        return result
    else:
        raise ValueError("combinations cannot be called with n or r")

a=permutations(n,r)
print(a)
B=combinations(n,r)
print(B)







