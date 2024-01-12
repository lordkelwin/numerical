from sympy import *
import numpy as np

'''
Steepest Descent Info

The variables are declared as x1, x2, x3, ..., xn depending on how many variables to be declared.
You can define your own function as long as it is bound by the Sympy library functions.

Always use '*' for multiplication and '**' when raising a term to a certain exponent

Common functions used:
    1. Natural exponent - exp()
    2. Natural logarithm - log() or ln()
    3. Trigonometric functions - sin(), cos(), tan(), cot(), sec(), csc()
    4. Hyperbolic functions - sinh(), cosh(), tanh(), coth(), sech(), csch()
    5. Inverse trigonometric functions - asin(), acos(), atan(), acot(), asec(), acsc()
    6. Inverse hyperbolic functions - asinh(), acosh(), atanh(), acoth(), asech(), acsch()

Constants used:
    1. pi
    2. exp()

When inputting a function
    Example: x^2 + 2x + 1
    f = x**2 + 2*x + 1

Function checking will be implemented later.
'''

varList = []  # Declare a list of variables to be used in the iteration
gradList = []  # Declare an empty list of function gradients
initVal = []  # Declare an empty of initial values
isNotTol = True  # Initialize that the initial condition is not optimized
isVarInput = True
isFuncInput = True
isTolInput = True

while isVarInput:
    try:
        noVar = int(input('Input number of variables: '))  # Asking for number of variables present in the equation
    except ValueError:
        print('Wrong value/input. Try again!')
    else:
        break

for i in range(1, noVar + 1):
    globals()[f'x{i}'] = Symbol(f'x{i}')
    varList.append(f'x{i}')

while isFuncInput:
    try:
        f = parse_expr(input('f = '))
    except ValueError:
        print('Wrong function or variable! Try again!')
    else:
        break

for i in range(len(varList)):
    initVal.append([float(input(f'Input an initial value for {varList[i]}: '))])

while isTolInput:
    try:
        tol = float(input('Enter a tolerance value: '))
    except ValueError:
        print('Wrong value/input! Please try again!')
    else:
        break


for var in varList:
    globals()[f'grad_{var}'] = f.diff(var)
    gradList.append(f.diff(var))

print(f'Gradient of f = {gradList}')

listH = []
for grad in gradList:
    rowH = []
    for var in varList:
        rowH.append(grad.diff(var))
    listH.append(rowH)

x = np.array(initVal)
H = np.zeros((len(varList), len(varList)))

n = 1
print('\n\n******STEEPEST DESCENT IMPLEMENTATION******')
header = f'{"i"}{"":10s}'
for i in range(len(varList)):
    header += f'{varList[i]:20s}'
print(header)

while isNotTol:
    linePrint = f'{n}{"":10s}'

    for h in range(len(varList)):
        for k in range(len(varList)):
            H[h][k] = listH[h][k].evalf(subs={varList[i]: float(x[i]) for i in range(len(varList))})

    listS = []
    for grad in gradList:
        listS.append([-grad.evalf(subs={varList[i]: float(x[i]) for i in range(len(varList))})])

    S = np.array(listS)
    St = -np.transpose(S)
    lamb = np.matmul(St, S) / np.matmul(np.matmul(St, H), S)
    x = x + lamb * S

    for j in range(len(varList)):
        linePrint += f'{str(x[j][0]):20.15s}'

    print(linePrint)

    n += 1
    if abs(S.any()) < tol:
        print('\n\nOptimal Values:')
        for i in range(len(varList)):
            print(f'{varList[i]} = {round(x[i][0], 10):0.15f}')
        break
