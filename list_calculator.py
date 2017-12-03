#######################################################
# This is a programme to create an object that will
# serve similarly to a scientific calculator with
# various functionality.
# Scripted by Andrew Doran-Sherlock 10361540
# 08 October 2017
#######################################################

import math


class Calculator(object): # define a calculator object
    def add(self, x, y): # define addition function
        return map(lambda x,y: x + y, x,y)


    def subtract(self, x, y): # define addition function
        return map(lambda x,y: x - y, x,y)

    def multiply(self, x, y):
        return map(lambda x,y: x * y, x,y)

    def divide(self, x, y):
        return map(lambda x,y: x / y, x,y)

    def exponential(self, x, y):
        return map(lambda x,y: x ** y, x,y)

    def square_root(self, x):
        return map(lambda x: math.sqrt(x), x)

    def sine(self, x):
        return map(lambda x: round(math.sin(x),5), x)

    def cosine(self, x):
        return map(lambda x: round(math.cos(x),5), x)

    def square(self, x):
        return map(lambda x: x*x, x)

    def cube(self, x):
        return map(lambda x: x*x*x, x)
            
    
