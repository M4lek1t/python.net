from sympy import diff, symbols, cos, sin, limit
from numpy import inf
# декоратор с аргументами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2
    return wrapper


def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 1
            for i in range(power):
               res *= func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@square
def f2(a, b, c):
    return a + b + c

# написать декоратор который считает провизодную функции в точке
def derivative(x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dx =  0.000000001
            res = (func(x +dx) - func(x)) / dx
            return res
        return wrapper
    return decorator


@pow(power=3)
def f3(c, g):
    return c - g

def ryad():
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = Limit(per, n, inf):
            return res
        return wrapper
    return decorator

@ryad
def f4(per)
    if res = 0
        return true
        elif res != 0
            return false






pow(1)
print(f2(1, 3, 0))
print(f3(10, 4))
print(f4(2n+1))
