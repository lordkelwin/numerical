from sympy import *


def secant(f, x1, x2, es):
    print('******SECANT METHOD******')
    print(f'{"i"}{"":10s}{"xi-1":20s}{"xi":20s}{"ea":15s}')
    isSec = True
    i = 3
    x = Symbol('x')
    f = parse_expr(f)
    while isSec:
        try:
            xi = x2 - (f.evalf(subs={x: x2})/(f.evalf(subs={x: x2}) - f.evalf(subs={x: x1})))*(x2 - x1)
        except OverflowError:
            print('Overflow error! Iteration will be stopped!')
            break
        else:
            ea = abs((f.evalf(subs={x: x2})/(f.evalf(subs={x: x2}) - f.evalf(subs={x: x1})))*(x2 - x1))
            x1 = x2
            x2 = xi
            isSec = ea > es
            print(f'{i-2}{x1:20.10f}{x2:20.10f}{ea:15.6f}')
        i += 1
    print(f'The iteration ends at i = {i - 3} with a root of x = {xi}')
