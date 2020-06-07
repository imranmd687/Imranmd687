import sympy as sym
from sympy import Subs, Function
import numpy as np
import math
import matplotlib.pyplot as plt

x = sym.Symbol('x')


def find_value_of_equation(expr, value):
    substitutedValue = expr.subs(x, value)
    return substitutedValue


def find_taylor_Expansion(equation, value):
    f0 = expr.subs(x, 0)
    print(f0)
    sum = f0
    valueat = expr.subs(x, value)
    i = 1

    xarray=[]
    yarray=[]

    def get_taylor_Expansion(equation, xvalue,avalue):
        f0 = equation.subs(x, xvalue)
        print(f0)
        sum = f0

        for j in range(1,3):
            equation = sym.diff(equation, x)
            newterm = ((equation.subs(x, xvalue)) / math.factorial(j))
            xadiff = (xvalue - avalue)**j
            newterm = newterm*xadiff

            sum += newterm
        return sum



    taylor_calculated_values=[]
    for i in np.arange(-1,6,0.5):
        yarray.append(find_value_of_equation(equation,i))
        xarray.append(i)
        if(i>= -1 and i < 1):
            taylor_calculated_values.append(get_taylor_Expansion(equation,i,0))
        elif (i>= 1 and i < 2) :
            taylor_calculated_values.append(get_taylor_Expansion(equation, i, 1))
        elif (i>= 2 and i < 3) :
            taylor_calculated_values.append(get_taylor_Expansion(equation, i, 2))
        elif (i>= 3 and i < 4) :
            taylor_calculated_values.append(get_taylor_Expansion(equation, i, 3))
        elif (i>= 4 and i < 5) :
            taylor_calculated_values.append(get_taylor_Expansion(equation, i, 4))
        elif (i>= 5 and i < 6) :
            taylor_calculated_values.append(get_taylor_Expansion(equation, i, 5))




    plt.plot(xarray,yarray,color="red")
    plt.plot(xarray,taylor_calculated_values)
    plt.ylabel('Nth order of the equation')
    plt.xlabel('X Value')
    plt.show()



if __name__ == "__main__":
    expr = 3 * x ** 3 + x ** 2 - 8 * x + 6
    find_value_of_equation(expr, 1)
    find_taylor_Expansion(expr, 1)