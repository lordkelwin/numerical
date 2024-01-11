from sympy import *


def modifiedSecant(f, perturbation, x0, es):
    print('******MODIFIED SECANT METHOD******')
    print(f'{"i"}{"":10s}{"xi":20s}{"ea":15s}')
    isSec = True
    i = 0
    x = Symbol('x')
    f = parse_expr(f)
    x1 = x0
    x2 = (perturbation + 1) * x0
    while isSec:
        '''try:
            xi = x1 - (f.evalf(subs={x: x1})/(f.evalf(subs={x: x2}) - f.evalf(subs={x: x1})))*perturbation
        except OverflowError:
            print('Overflow error! Iteration will be stopped!')
            break
        else:
            if i == 0:
                ea = 100
            else:
                ea = abs((xi - x1)/xi) * 100
            x1 = xi
            x2 = xi * perturbation
            isSec = ea > es'''
        if i == 0:
            ea = 100
        else:
            xi = x1 - (f.evalf(subs={x: x1}) / (f.evalf(subs={x: x2}) - f.evalf(subs={x: x1}))) * perturbation * x1
            if xi > 1000000:
                print('Overflow error! Iteration will be stopped!')
                break
            ea = abs((xi - x1) / xi) * 100
            isSec = ea > es
            x1 = xi
            x2 = xi * (1 + perturbation)
        print(f'{i}{x1:20.10f}{ea:15.6f}')
        i += 1
    print(f'The iteration ends at i = {i - 1} with a root of x = {xi}')
