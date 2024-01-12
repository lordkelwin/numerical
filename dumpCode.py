from inputPoly import *
from Newton_Raphson import *
from fixed_point import *
from secantMethod import *
from modifiedSecant import *
from sympy import *


selValid = True

while selValid:
    sel = input('Select to input a polynomial (1) or any function (2): ')
    if sel not in ('1', '2'):
        print('Input either 1 or 2. Please try again.')
    else:
        selValid = False

xValid = True
esValid = True
if sel == '1':
    nValid = True

    while nValid:
        try:
            n = int(input('Enter polynomial degree n = '))
        except ValueError:
            print('Value Error! Please try again!')
        else:
            nValid = False
    f = inputPoly(n)

elif sel == '2':
    x = Symbol('x')
    f = input('f(x) = ')

while xValid:
    try:
        x0 = float(input('Enter initial value x0 = '))
    except ValueError:
        print('Value Error! Please try again!')
    else:
        xValid = False

while esValid:
    try:
        es = float(input('Enter error tolerance es = '))
    except ValueError:
        print('Value Error! Please try again!')
    else:
        esValid = False

methodValid = True

while methodValid:
    method = input('Select between:\n'
                   '\ta. Fixed-Point Method\n'
                   '\tb. Newton-Raphson Method\n'
                   '\tc. Secant Method\n'
                   '\td. Modified Secant Method: ')
    if method not in ('a', 'b', 'c', 'd'):
        print('Wrong input! Please try again!')
    else:
        methodValid = False

if method == 'a':
    fixedPoint(sel, f, x0, es)
elif method == 'b':
    newtonRaphson(sel, f, x0, es)
elif method == 'c':
    x2Valid = True
    while x2Valid:
        try:
            x1 = float(input('Enter initial value x1 = '))
        except ValueError:
            print('Value Error! Please try again!')
        else:
            x2Valid = False
    secant(f, x0, x1, es)
elif method == 'd':
    pertubValid = True
    while pertubValid:
        try:
            p = float(input('Enter a value of small perturbation fraction: '))
        except ValueError:
            print('Value Error! Please try again!')
        else:
            break
    modifiedSecant(f, p, x0, es)
