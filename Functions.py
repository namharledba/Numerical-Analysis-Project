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


def valid(xu, xl, equ):
    x = sp.symbols('x')
    fx = parse_function(equ)
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)
    return fxu * fxl < 0


def valid_error(expected_error):
    return 0 < expected_error < 100


def simple_fixed_point(frist_initial, equ, expected_error):
    x = sp.symbols('x')
    fx = parse_function(equ)
    highest_power = sp.degree(fx)
    highest_coefficient = fx.coeff(x ** highest_power)

    reset = fx - (highest_coefficient * x ** highest_power)
    if highest_coefficient < 0:
        gx_expr = (-reset / highest_coefficient) ** (1 / highest_power)
    else:
        gx_expr = (reset / highest_coefficient) ** (1 / highest_power)
    x_value = float(frist_initial)
    error = 100
    i = 0
    df = pd.DataFrame(columns=['X', 'gx', 'Error'])
    while error != expected_error:
        gx = gx_expr.subs(x, x_value)

        if i == 0:
            new_row_data = pd.DataFrame([{
                'X': round(x, 3), 'gx': round(gx, 5), 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
                'X': round(x, 3), 'gx': round(gx, 5), 'Error': round(error, 5)
            }])

        df = pd.concat([df, new_row_data], ignore_index=True)
        if error <= expected_error: break
        error = abs((gx - x_value) / gx) * 100
        x_value = gx
        i += 1
    return df

def bi_section(xl, xu, equ, expected_error, iter = 50):
    x = sp.symbols('x')
    fx = parse_function(equ)
    xr = 0.00
    i = 0
    error = 100
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)
    df = pd.DataFrame(columns=['Xl', 'Fxl', 'Xu', 'Fxu', 'Xr', 'Fxr', 'Error'])

    while valid(xu, xl, equ):
        if (not valid(xu, xl, equ)):
            return 1
        xr_old = xr
        xr = (xl + xu) / 2.0
        fxr = fx.subs(x, xr)

        if i == 0 :

            new_row_data = pd.DataFrame([{
                'Xl': xl, 'Fxl': fxl, 'Xu': xu, 'Fxu': fxu,
                'Xr': xr, 'Fxr': fxr, 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
            'Xl': xl, 'Fxl':fxl, 'Xu': xu, 'Fxu': fxu,
            'Xr': xr, 'Fxr': fxr, 'Error': error
            }])
            error = abs((xr - xr_old) / xr) * 100
        df = pd.concat([df, new_row_data], ignore_index=True)
        if fxr * fxl < 0:
            xu = xr
            fxu = fx.subs(x, xu)
        elif fxr * fxl > 0:
            xl = xr
            fxl = fx.subs(x, xl)
        else:
            break
        if error <= expected_error or i >= iter:
            break
        i += 1
    return df


def false_position(xl, xu, equ, expected_error):
    x = sp.symbols('x')
    fx = parse_function(equ)
    xr = 0.00
    i = 0
    error = 100
    fxl = fx.subs(x, xl)
    fxu = fx.subs(x, xu)
    df = pd.DataFrame(columns=['Xl', 'Fxl', 'Xu', 'Fxu', 'Xr', 'Fxr', 'Error'])

    while valid(fxu, fxl, equ):
        xr_old = xr
        xr = xu - ((fxu * (xl - xu)) / (fxl - fxu))
        fxr = fx.subs(x, xr)
        if i == 0 :
            new_row_data = pd.DataFrame([{
                'Xl': round(xl, 3), 'Fxl': round(fxl, 5), 'Xu': round(xu, 3), 'Fxu': round(fxu, 5),
                'Xr': round(xr, 3), 'Fxr': round(fxr, 5), 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
            'Xl': round(xl, 3), 'Fxl': round(fxl, 5), 'Xu': round(xu, 3), 'Fxu': round(fxu, 5),
            'Xr': round(xr, 3), 'Fxr': round(fxr, 5), 'Error': round(error, 5)
            }])
            error = abs((xr - xr_old) / xr) * 100
        df = pd.concat([df, new_row_data], ignore_index=True)

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
    return df


def newton_method(initial, equ, expected_error):
    x = sp.symbols('x')
    fx = parse_function(equ)
    dfx = sp.diff(fx, x)
    xi = round(initial, 3)
    error = 100
    i = 0
    df = pd.DataFrame(columns=['X', 'f(x)', "f'(x)",'Error'])
    while True:

        fx_val = fx.subs(x, xi)
        dfx_val = dfx.subs(x, xi)
        xi_plus1 = round(xi - (fx_val / dfx_val), 3)

        if i == 0:
            new_row_data = pd.DataFrame([{
                'X' : xi, 'f(x)' : fx_val, "f'(x)":dfx_val, 'Error':"---"
            }])
        else:
            new_row_data = pd.DataFrame([{
                'X': xi, 'f(x)': fx_val, "f'(x)": dfx_val, 'Error': error
            }])
        df = pd.concat([df, new_row_data], ignore_index=True)

        if error <= expected_error: break

        error = round(abs((xi_plus1 - xi) / xi_plus1) * 100, 3)
        xi = xi_plus1
        i += 1
    return df

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
    temp_matrix = np.array(ab, float)
    shape = temp_matrix.shape
    no_columns = shape[1]
    no_rows = shape[0]
    a = temp_matrix[:, :-1]
    b = temp_matrix[:, -1]
    x = zeros(no_rows)

    for i in range(no_rows):
        b[i] = ab[i][-1]

    for i in range(no_rows):
        for j in range(no_columns - 1):
            a[i][j] = ab[i][j]

    for k in range(no_rows - 1):
        for i in range(k + 1, no_rows):
            if a[i][k] == 0: continue
            factor = a[i][k] / a[k][k]
            for j in range(k, no_columns - 1):
                a[i][j] = a[i][j] - (a[k][j] * factor)
            b[i] = b[i] - (b[k] * factor)

    x[no_rows - 1] = b[no_rows - 1] / a[no_rows - 1][no_rows - 1]

    for i in range(no_rows - 1, -1, -1):
        sum_x = 0
        for j in range(i + 1, no_rows):
            sum_x += a[i][j] * x[j]
            x[i] = (b[i] - sum_x) / a[i][i]


def lu_decomposition(ab):
    temp_matrix = np.array(ab, float)
    n = temp_matrix.shape[0]
    a = temp_matrix[:, :-1]
    b = temp_matrix[:, -1]

    l = np.eye(n)
    u = np.zeros((n, n))

    for i in range(n):

        for k in range(i, n):
            sum_lu = sum(l[i][j] * u[j][k] for j in range(i))
            u[i][k] = a[i][k] - sum_lu

        for k in range(i + 1, n):
            sum_lu = sum(l[k][j] * u[j][i] for j in range(i))
            l[k][i] = (a[k][i] - sum_lu) / u[i][i]

    y = np.zeros(n)
    for i in range(n):
        sum_ly = sum(l[i][j] * y[j] for j in range(i))
        y[i] = b[i] - sum_ly

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ux = sum(u[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_ux) / u[i][i]

    return l, u, x