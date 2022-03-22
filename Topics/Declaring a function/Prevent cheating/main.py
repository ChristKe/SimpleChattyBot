import math
def new_math_factorial(_):
    print("Don't cheat!")
math.factorial = new_math_factorial
# your code here
x = 23
# don't delete this line, please
math.factorial(x)
