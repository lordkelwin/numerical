# from sympy import *


def bisection(f, x0, x1, e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        if step == 1:
            x_old = 0
            x2 = (x1 + x0) / 2
        else:
            x_old = x2
            x2 = (x1 + x0)/2
        print('Iteration %d, x2 = %0.6f and e = %0.6f' % (step, x2, abs((x2 - x_old)/x2*100)))
        fx0 = f.evalf(subs={x: x0})
        fx2 = f.evalf(subs={x: x2})

        if fx0 * fx2 < 0:
            x1 = x2
        else:
            x0 = x2

        step += 1
        condition = abs((x2 - x_old)/x2) > e

    print('\nRequired Root is: %0.8f' % x2)

'''
x = Symbol('x')
f = input('f(x) = ')
x0 = float(input('Lower Bound: '))
x1 = float(input('Upper Bound: '))
e = float(input('Tolerable Error: '))
f = parse_expr(f)
fx0 = f.evalf(subs={x: x0})
fx1 = f.evalf(subs={x: x1})
if x0 > x1:
    print('Lower Bound is Greater than Upper Bound! Try Again!')
else:
    if fx0 * fx1 > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        bisection(f, x0, x1, e)
'''
