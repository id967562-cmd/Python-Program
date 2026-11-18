#TODO:1)Import from Module -- Allow importing specific function,classes or variable rather than whole module
from math import sqrt,factorial
print(sqrt(16))
print(factorial(6))

#TODO:2)Import ALL Names -- '*' Imports everything from a module into the current namespaces
from math import *
print(sum([1,4,5,6,7]))
print(prod([2,3,4,5]))

#TODO:3)Import With Alias -- shorten a module's name using as
import math as m
print(m.pi)

