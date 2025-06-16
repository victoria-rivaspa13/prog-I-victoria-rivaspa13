def ordena(num1, num2):
    if num1 > num2:
        return num2, num1
    else:
        return num1, num2

print(ordena(120,80))

def calcula(num1, num2, operando):
    resultado =""
    if operando == "+":
        resultado = num1 + num2
    if operando == "-":
        resultado = num1 - num2
    if operando == "*":
        resultado = num1 * num2
    if operando == "/":
        resultado = num1 / num2
    return resultado

def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def number_to_month(month):
    if month == 1:
        return "enero"
    if month == 2:
        return "febrero"
    if month == 3:
        return "marzo"
    if month == 4:
        return "abril"
    if month == 5:
        return "mayo"
    if month == 6:
        return "junio"
    if month == 7:
        return "julio"
    if month == 8:
        return "agosto"
    if month == 9:
        return "septiembre"
    if month == 10:
        return "octubre"
    if month == 11:
        return "noviembre"
    if month == 12:
        return "diciembre"
    else:
        return "error"

import math
def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b+math.sqrt(discriminant))/2*a
        r2 = (-b-math.sqrt(discriminant))/2*a
        return f"{r1, r2}"
    elif discriminant == 0:
        r1 = (-b/2*a)
        return f"({r1})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y = a * x**2 + b * x + c
    return y

def to_string(a, b, c):
    if a == 0 and not b == 0 and not c == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and not c == 0 and not a == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0 and not b == 0 and not a == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and not c == 0:
        return f"f(x) = {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a == 0:
        return f"f'(x) = {b}"
    elif b==0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"

