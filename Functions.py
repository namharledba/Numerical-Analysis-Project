import sympy as sp
import sqlite3 as sql


db = sql.connect("Numerical_Analysis.db")
cr = db.cursor()

cr.execute("CREATE TABLE if not exists polynomials(xl DOUBLE, xu DOUBLE, equ TEXT, expected_error DOUBLE)")
cr.execute("CREATE TABLE if not exists polynomials2( frist_initial DOUBLE, equ TEXT, expected_error DOUBLE)")


def display (i,xl,fxl,xu,fxu,xr,fxr,error) :
    print(f"iteration :{i} | xl = {xl:.3f} | f(xl) = {fxl:.3f} | xu = {xu:.3f}|f(xu) = {fxu:.3f} | xr = {xr:.3f} |"
          f" f(xr) = {fxr:.3f} |error = {error:.3f} %")

def valid(fxu, fxl):
        return fxu * fxl < 0

def simple_fixed_point(frist_initial, equ, expected_error):
    input_tuple = (frist_initial, equ, expected_error)
    cr.execute("insert into polynomials2 values(?,?,?) ",input_tuple)
    cr.execute("select * from polynomials2")
    db.commit()
    db.close()
    x = sp.symbols('x')
    fx = sp.sympify(equ)
    highest_power = sp.degree(fx)
    coeff_highest = fx.coeff(x ** highest_power)

    reset = fx - (coeff_highest * x ** highest_power)
    if coeff_highest < 0 :
        gx_expr = (-reset / coeff_highest) ** (1 / highest_power)
    else :
        gx_expr = (reset / coeff_highest) ** (1 / highest_power)
    x_value = float(frist_initial)
    error = 100
    i = 0

    while error != expected_error :
        gx = gx_expr.subs(x, x_value)
        if i == 0:
            print(f"i = {i} | X = {x_value:.3f} | gx = {gx:.3f} | error = ____")
        else :
            print(f"i = {i} | X = {x_value:.3f} | gx = {gx:.3f} | error = {error:.3f} %")
        if error <= expected_error: break
        error = abs((gx - x_value) / gx) * 100
        x_value = gx
        i += 1


def bi_section(xl, xu, equ, expected_error):
    input_tuple = (xl, xu, equ, expected_error)
    cr.execute("insert into polynomials values(?,?,?,?) ",input_tuple)
    cr.execute("select * from polynomials")
    db.commit()
    db.close()
    x = sp.symbols('x')
    fx = sp.sympify(equ)
    xr= 0.00
    i = 0
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)

    while valid(fxu,fxl) :
        if not valid(fxu,fxl):
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
        if error <= expected_error: break
        i+=1


def false_position(xl, xu, equ, expected_error):
    input_tuple = (xl, xu, equ, expected_error)
    cr.execute("insert into polynomials values(?,?,?,?) ",input_tuple)
    cr.execute("select * from polynomials")
    db.commit()
    db.close()
    x = sp.symbols('x')
    fx = sp.sympify(equ)
    xr = 0.00
    i = 0
    fxl = fx.subs(x, xl)
    fxu = fx.subs(x, xu)

    while valid(fxu,fxl) :
        if not valid(fxu,fxl):
            print("The function has no solution...")
            break

        xr_old = xr
        xr = xu - ((fxu * (xl - xu)) / (fxl - fxu))
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
        if error <= expected_error: break
        i += 1

def newton_method(initial, equ, expected_error):
    x = sp.symbols('x')
    fx = sp.sympify(equ)
    dfx = sp.diff(fx, x)

    x_value = float(initial)
    error = 100
    i = 0

    while error != expected_error:
        fx_val = float(fx.subs(x, x_value))
        dfx_val = float(dfx.subs(x, x_value))

        xr = x_value - (fx_val / dfx_val)


        if i == 0:
            print(f"iteration :{i} | x = {x_value:.6f} | f(x) = {fx_val:.6f} | f'(x) = {dfx_val:.6f} | error = ____")
        else:
            print(f"iteration :{i} | x = {x_value:.6f} | f(x) = {fx_val:.6f} | f'(x) = {dfx_val:.6f} | error = {error:.6f}%")

        error = abs((xr - x_value) / xr) * 100

        if error <= expected_error:
            break

        x_value = xr
        i += 1

def se_cant(xi, xi_1, equ, expected_error):

    x = sp.symbols('x')
    fx = sp.sympify(equ)

    error = 100
    i = 0
    while error != expected_error:

        xi_old = xi

        fxi = float(fx.subs(x, xi))
        fxi_1 = float(fx.subs(x, xi_1))

        xi_new = xi - (fxi * (xi_1 - xi)) / (fxi_1 - fxi)

        error = abs((xi_new - xi_old) / xi_new) * 100

        print(f"iteration:{i}|{xi_1:.3f}|{fxi_1:.3f}|{xi:.3f}|{fxi:.3f}|{error:.3f}")

        xi_1 = xi
        xi = xi_new

        i += 1

