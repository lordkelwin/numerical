import numpy as np
from sympy import *


def fixedPoint(z, f, x0, es):
    isCont = True
    xi = 0
    i = 0

    print('\n\n******FIXED POINT METHOD******')
    print(f'{"i"}{"":10s}{"xi":15s}{"ea":15s}')

    if z == '1':
        while isCont:
            if i == 0:
                ea = '\t\t-'
            else:
                xi = round(f(x0), 6)
                ea = round(abs((xi - x0) / xi) * 100, 6)
                isCont = ea > es
                x0 = xi
            print(f'{i}\t\t\t{x0}\t{ea}')
            i += 1
    elif z == '2':
        x = Symbol('x')
        x1 = Symbol('x1')
        f = parse_expr(f)
        f = solve(Eq(f, 0), x)
        if len(f) > 1:
            f = f[len(f)-1]
        else:
            f = f[0]

        while isCont:
            if i == 0:
                ea = 100
            else:
                '''try:
                    xi = round(f.evalf(subs={x: x0}), 6)
                except OverflowError:
                    print('Overflow Error! Iterative process results in divergence, the process will be stopped!')
                    isCont = False
                else:
                    ea = round(abs((xi - x0) / xi) * 100, 6)
                    isCont = ea > es
                    x0 = xi'''
                xi = f.evalf(subs={x1: x0})
                if abs(xi) > 1000000:
                    print('Overflow Error! Iterative process results in divergence, the process will be stopped!')
                    break
                ea = abs((xi - x0) / xi) * 100
                isCont = ea > es
                x0 = xi
            print(f'{i}{x0:15.6f}{ea:15.6f}')
            i += 1
    print(f'The iteration ends at i = {i - 1} with a root of x = {xi}')
