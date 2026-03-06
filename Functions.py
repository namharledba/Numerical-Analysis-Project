import sympy
from sympy import symbols, sympify, solve, Eq

def display (i,xl,fxl,xu,fxu,xr,fxr,error) :
    if i == 1 :
        print(f"iteration :{i} | xl = {xl:.3f} | f(xl) = {fxl:.3f} | xu = {xu:.3f}|f(xu) = {fxu:.3f} | xr = {xr:.3f} |"
          f" f(xr) = {fxr:.3f} |error = {"____"}")
    else :
        print(f"iteration :{i} | xl = {xl:.3f} | f(xl) = {fxl:.3f} | xu = {xu:.3f}|f(xu) = {fxu:.3f} | xr = {xr:.3f} |"
              f" f(xr) = {fxr:.3f} |error = {error:.3f} ")

def not_valid(fxu, fxl):
        return fxu * fxl > 0


def simple_fixed_point(frist_initial, equ, expected_error):
    x = symbols('x')
    fx = sympify(equ)
    highest_power = sympy.degree(fx)
    coeff_highest = fx.coeff(x ** highest_power)
    reset = fx - (coeff_highest * x ** highest_power)
    gx_expr = (reset / coeff_highest) ** (1 / highest_power)
    x_value = float(frist_initial)
    error = 100
    i = 1

    while error != expected_error :
        gx = gx_expr.subs(x, x_value)
        if i == 1:
            print(f"i = {i} | X = {x_value:.3f} | gx = {gx:.3f} | error = ____")
        else :
            print(f"i = {i} | X = {x_value:.3f} | gx = {gx:.3f} | error = {error:.3f}")
        if error < expected_error: break
        error = abs((gx - x_value) / gx) * 100
        x_value = gx
        i += 1


def bi_section(xl, xu, equ, expected_error):
    x = symbols('x')
    fx = sympify(equ)
    xr= 0.00
    error = 100
    i = 1
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)

    while error != expected_error :
        if not_valid(fxu, fxl):
            print("The function has no solution...")
            break
        xr_old = xr
        xr = (xl + xu) / 2.0
        fxr = fx.subs(x, xr)

        error = abs((xr - xr_old) / xr) * 100
        display(i,xl,fxl,xu,fxu,xr,fxr,error)
        if fxr * fxl < 0:
            xu = xr
            fxu = fx.subs(x, xu)
        elif fxr * fxl > 0:
            xl = xr
            fxl = fx.subs(x, xl)
        else:
            break
        if error < expected_error: break
        i+=1


def false_position(xl, xu, equ, expected_error):
    x = symbols('x')
    fx = sympify(equ)
    xr = 0.00
    error = 100
    i = 1
    while error != expected_error:
        xr_old = xr

        fxl = float(fx.subs(x, xl))
        fxu = float(fx.subs(x, xu))

        if fxu * fxl > 0:
            print("The function has no solution...")
            break

        xr = float(xu - ((fxu * (xl - xu)) / (fxl - fxu)))
        fxr = float(fx.subs(x, xr))
        error = abs((xr - xr_old) / xr) * 100

        display(i,xl,fxl,xu,fxu,xr,fxr,error)
        if fxr * fxl < 0:
            xu = xr
        elif fxr * fxu < 0:
            xl = xr
        else:
            break
        if error < expected_error: break
        i += 1