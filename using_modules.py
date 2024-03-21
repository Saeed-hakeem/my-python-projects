import functions

functions.printName("yankee")
from math import sqrt
print(sqrt(100))


# Import the 'random' module, which is a built-in module for random number generation
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 20)
print("Random Number:", random_number)

# Import the 'math' module with the alias 'm'
import math as m

# Use functions from the 'math' module with the alias
result = m.sqrt(625)
print("Square root of 625:", result)

#All the functions and constants can be imported using *

from math import *
print(pi)
print(factorial(6))

