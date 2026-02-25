from sympy import symbols, sympify, solve, Eq
import math

def simple_fixed_point(equ,frist_initial, expected_error):     #the function isn't working, can't solve equtions correctly 
    x = symbols('x')
    fx = sympify(equ)
    x_value = float(frist_initial)
    poly = fx.as_poly()
    deg = poly.degree()
    highest_term = x ** deg
    gx = (solve(Eq(fx, 0), highest_term)[0])**(1/deg)
    result = gx.subs(x,x_value)
    error = 100
    i = 0
    while error > expected_error :
        print(f"iteration: {i} | X = {x_value} | g(x) = {gx} | error = {error}")
        temp = x_value
        x_value = gx.subs(x_value,temp)
        error = abs((x_value - temp)/x_value)
        i += 1


def bi_section(xl, xu, equ, expected_error):                 #this functioins can't handle large and inaccurate inputs
    x = symbols('x')
    fx = sympify(equ)
    xr= 0.00
    error = 100
    i = 0
    while error > expected_error :
        xr_old = xr
        xr = float((xl + xu) / 2.0)
        fxr= float(fx.subs(x,xr))
        fxl = float(fx.subs(x, xl))
        fxu = float(fx.subs(x, xu))

        print(f"i = {i} | xl = {round(xl,3)} | f(xl) = {round(fxl,3)} | xu = {round(xu,3)}|f(xu) = {round(fxu,3)} | xr = {round(xr,3)} | f(xr) = {round(fxr,3)} |error = {round(error,3)}")
        if fxr * fxl < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xr - xr_old )/xr)*100
        i+=1
