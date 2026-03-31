import sympy as sp
import sqlite3 as sql
import numpy as np
from numpy.matlib import zeros
import pandas as pd
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

def parse_function(equ):
    equ = equ.replace("^", "**")
    transformations = standard_transformations + (implicit_multiplication_application,)
    return sp.parse_expr(equ, transformations=transformations)

db = sql.connect("Numerical_Analysis.db")
cr = db.cursor()


def valid(fxu, fxl):
        return fxu * fxl < 0



def simple_fixed_point(frist_initial, equ, expected_error):
    x = sp.symbols('x')
    fx = parse_function(equ)
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
    x = sp.symbols('x')
    fx = parse_function(equ)
    xr= 0.00
    i = 0
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)
    df = pd.DataFrame(columns=['Xl', 'Fxl', 'Xu', 'Fxu', 'Xr', 'Fxr', 'Error'])
    while valid(fxu,fxl) :
        xr_old = xr
        xr = (xl + xu) / 2.0
        fxr = fx.subs(x, xr)
        error = abs((xr - xr_old) / xr) * 100
        new_row_data = pd.DataFrame([{'Xl':round(xl,3),'Fxl':round(fxl,3) ,'Xu':round(xu,3),'Fxu':round(fxu,3),'Xr':round(xr,3),'Fxr':round(fxr,3),'Error':round(error,5)}])
        df = pd.concat([df,new_row_data],ignore_index=True)

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
    return df


def false_position(xl, xu, equ, expected_error):
    x = sp.symbols('x')
    fx = parse_function(equ)
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

    x       =  sp.symbols('x')
    fx      =  parse_function(equ)
    dfx     =  sp.diff(fx, x)
    xi      =  round(initial,3)
    error   =  100
    i       =  0

    while True:

        fx_val   = fx.subs( x , xi )
        dfx_val  = dfx.subs( x , xi )
        xi_plus1 = round(xi - ( fx_val / dfx_val ),3)

        if i == 0:
            print(f"iteration :{i} | x = {xi} | f(x) = {round(fx_val,4)} | f'(x) = {round(dfx_val,3)} | error = ____")
        else:
            print(f"iteration :{i} | x = {xi} | f(x) = {round(fx_val,4)} | f'(x) = {round(dfx_val,3)} | error = {error}%")

        if error <= expected_error: break

        error = round(abs((xi_plus1 - xi) / xi_plus1) * 100,3)
        xi    = xi_plus1
        i    += 1

def se_cant(xi, xi_1, equ, expected_error):

    x = sp.symbols('x')
    fx = parse_function(equ)

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



def gauss_elimination(ab):
    temp_matrix = np.array(ab,float)
    shape       = temp_matrix.shape
    no_columns  = shape[1]
    no_rows     = shape[0]
    a = temp_matrix[:, :-1]
    b = temp_matrix[:, -1]
    x = zeros(no_rows)

    for i in range(no_rows):
            b[i] = ab[i][-1]

    for i in range(no_rows):
        for j in range(no_columns-1):
            a[i][j] = ab[i][j]


    for k in range(no_rows-1):
        for i in range(k+1, no_rows):
            if a[i][k] == 0: continue
            factor = a[i][k] / a[k][k]
            for j in range(k,no_columns-1):
                a[i][j] = a[i][j] - (a[k][j] * factor)
            b[i] = b[i] - (b[k] * factor)

    x[no_rows-1] = b[no_rows-1] / a[no_rows-1][no_rows-1]

    for i in range(no_rows - 1, -1, -1):
        sum_x = 0
        for j in range(i + 1, no_rows):
                sum_x += a[i][j] * x[j]
                x[i] = (b[i] - sum_x) / a[i][i]
