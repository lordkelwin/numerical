import numpy as np
from sympy import *


def newtonRaphson(z, f, x0, es):
    isCont = True
    xi = 0
    i = 0

    print('\n\n******NEWTON-RAPHSON METHOD******')
    print(f'{"i"}{"":10s}{"xi":20s}{"ea":15s}')

    if z == '1':
        fder = np.polyder(f)
        while isCont:
            if i == 0:
                ea = '\t\t-'
            else:
                xi = round(x0 - (f(x0) / fder(x0)), 6)
                ea = round(abs((xi - x0) / xi) * 100, 6)
                isCont = ea > es
                x0 = xi
            print(f'{i}\t\t\t{x0}\t{ea}')
            i += 1
    elif z == '2':
        x = Symbol('x')
        f = parse_expr(f)
        fder = diff(f)
        while isCont:
            if i == 0:
                ea = 100
            else:
                xi = x0 - (f.evalf(subs={x: x0}) / fder.evalf(subs={x: x0}))
                ea = abs((xi - x0) / xi) * 100
                isCont = ea > es
                x0 = xi
            print(f'{i}{x0:20.10f}{ea:15.6f}')
            i += 1
    print(f'The iteration ends at i = {i - 1} with a root of x = {xi}')
