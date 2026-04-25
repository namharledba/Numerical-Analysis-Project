import sympy as sp
import sqlite3 as sql
import numpy as np
from numpy.matlib import zeros
import pandas as pd
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

def set_xr(xl, xu):
        result = (xl + xu) / 2
        return result


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


def set_max_iterations_(max_iterations):
    if max_iterations == 0:
        return 50
    if max_iterations < 0:
        return None
    else:
        return max_iterations


def validate_function(equ):
    try:
        expr = parse_function(equ)
        x = sp.symbols('x')
        
        free_symbols = expr.free_symbols
        if free_symbols - {x}:
            return False, f"Unknown variables: {free_symbols - {x}}"
        
        expr.subs(x, 1.0)
        return True, None
    except Exception as e:
        return False, str(e)

def simple_fixed_point(initial, equ, expected_error, max_iterations):
    
    x = sp.symbols('x')
    fx = parse_function(equ)
    iterations = set_max_iterations_(max_iterations)

    highest_power = sp.degree(fx)
    highest_coefficient = fx.coeff(x ** highest_power)
    reset = fx - (highest_coefficient * x ** highest_power)
    if highest_coefficient < 0:
        gx_expr = (-reset / highest_coefficient) ** (1 / highest_power)
    else:
        gx_expr = (reset / highest_coefficient) ** (1 / highest_power)
    
    xi = float(initial)
    error = 100

    df = pd.DataFrame(columns=['X', 'gx', 'Error'])
    while True:
        
        gx = gx_expr.subs(x, xi)
        gx = float(abs(gx.evalf())) 

        if iterations == set_max_iterations_(max_iterations) :
            new_row_data = pd.DataFrame([{
                'X': xi, 'gx': gx, 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
                'X': xi, 'gx': gx, 'Error': error
            }])

        df = pd.concat([df, new_row_data], ignore_index=True)
        
        if error <= expected_error or iterations == 0:
            break

        error = abs((gx - xi) / gx) * 100
        xi = gx
        iterations -= 1
    if df.empty: return None
    else: 
        df = df.apply(pd.to_numeric, errors='ignore') 
        return df


def bi_section(xl, xu, equ, expected_error, max_iterations):
    
    x = sp.symbols('x')
    fx = parse_function(equ)
    
    iterations = set_max_iterations_(max_iterations)
    xr_old = 0.00
    fxu = fx.subs(x, xu)
    fxl = fx.subs(x, xl)
    
    df = pd.DataFrame(columns=['xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error'])

    while valid(xu, xl, equ):
        xr = set_xr(xl, xu)
        fxr = fx.subs(x, xr)
        error = abs((xr - xr_old) / xr) * 100

        if iterations == set_max_iterations_(max_iterations) :
            new_row_data = pd.DataFrame([{
                'xl': float(xl), 'f(xl)': float(fxl), 'xu': float(xu), 'f(xu)': float(fxu),
                'xr': float(xr), 'f(xr)': float(fxr), 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
            'xl': float(xl), 'f(xl)': float(fxl), 'xu': float(xu), 'f(xu)': float(fxu),
            'xr': float(xr), 'f(xr)': float(fxr), 'Error': float(error)
            }])

        df = pd.concat([df, new_row_data], ignore_index=True)
        
        if fxr * fxl < 0:
            xu = xr
            fxu = fx.subs(x, xu)
        elif fxr * fxl > 0:
            xl = xr
            fxl = fx.subs(x, xl)       
        if error <= expected_error or iterations == 0:
            break
        iterations -= 1 
        xr_old = xr
    
    if df.empty: return None
    else: return df


def false_position(xl, xu, equ, expected_error,max_iterations):
    
    x = sp.symbols('x')
    fx = parse_function(equ)

    iterations = set_max_iterations_(max_iterations)
    xr_old = 0.00

    fxl = fx.subs(x, xl)
    fxu = fx.subs(x, xu)
    df = pd.DataFrame(columns=['xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error'])
    while valid(xu, xl, equ):
        
        xr = xu - ((fxu * (xl - xu)) / (fxl - fxu))
        fxr = fx.subs(x, xr)
        error = abs((xr - xr_old) / xr) * 100

        if iterations == set_max_iterations_(max_iterations) :
            new_row_data = pd.DataFrame([{
                'xl': float(xl), 'f(xl)': float(fxl), 'xu': float(xu), 'f(xu)': float(fxu),
                'xr': float(xr), 'f(xr)': float(fxr), 'Error': "---"
            }])
        else:
            new_row_data = pd.DataFrame([{
            'xl': float(xl), 'f(xl)': float(fxl), 'xu': float(xu), 'f(xu)': float(fxu),
            'xr': float(xr), 'f(xr)': float(fxr), 'Error': float(error)
            }])

        df = pd.concat([df, new_row_data], ignore_index=True)

        if fxr * fxl < 0:
            xu = xr
            fxu = fx.subs(x, xu)
        elif fxr * fxl > 0:
            xl = xr
            fxl = fx.subs(x, xl)

        if error <= expected_error or iterations == 0:
            break
        iterations -= 1
        xr_old = xr
    
    if df.empty: return None
    else: return df


def newton_method(initial, equ, expected_error,max_iterations):
    
    x = sp.symbols('x')
    fx = parse_function(equ)
    dfx = sp.diff(fx, x)
    
    xi = float(initial)
    error = 100
    iterations = set_max_iterations_(max_iterations)
    df = pd.DataFrame(columns=['X', 'f(x)', "f'(x)",'Error'])
    while True:

        fx_val = fx.subs(x, xi)
        dfx_val = dfx.subs(x, xi)
        xi_plus1 = xi - (fx_val / dfx_val)

        if iterations == set_max_iterations_(max_iterations):
            new_row_data = pd.DataFrame([{
                'X' : float(xi), 'f(x)' : float(fx_val), "f'(x)":float(dfx_val), 'Error':"---"
            }])
        else:
            new_row_data = pd.DataFrame([{
                'X': float(xi), 'f(x)': float(fx_val), "f'(x)": float(dfx_val), 'Error': float(error)
            }])
        df = pd.concat([df, new_row_data], ignore_index=True)

        if error <= expected_error or iterations == 0:
            break
        error = abs((xi_plus1 - xi) / xi_plus1) * 100
        xi = xi_plus1
        iterations -= 1
    
    if df.empty: return None
    else: return df


def se_cant(xi_1, x0, equ, expected_error,max_iterations):
    
    x = sp.symbols('x')
    fx = parse_function(equ)

    iterations = set_max_iterations_(max_iterations)
    df = pd.DataFrame(columns=['xi-1', 'f(xi-1)', 'xi', 'f(xi)', 'Error'])

    while True:
        fxi_1 = fx.subs(x, xi_1)
        fx0 = fx.subs(x, x0)
        xiplus1 = x0 - fx0 * (( xi_1 - x0) / (fxi_1 - fx0))
        error = abs((x0 - xi_1) / x0) * 100
        if iterations == set_max_iterations_(max_iterations):
            new_row_data = pd.DataFrame([{
                'xi-1' : float(xi_1), 'f(xi-1)' : float(fxi_1), 'xi' : float(x0), 'f(xi)' : float(fx0), 'Error':"---"
            }])
        else:
            new_row_data = pd.DataFrame([{
                'xi-1': float(xi_1), 'f(xi-1)': float(fxi_1), 'xi': float(x0), 'f(xi)': float(fx0), 'Error': float(error)
            }])
        df = pd.concat([df, new_row_data], ignore_index=True)
        xi_1 = x0
        x0 = xiplus1

        if error <= expected_error or iterations == 0:
            break
        iterations -= 1
    if df.empty: return None
    else: return df


def gauss_elimination(ab):
    temp_matrix = np.array(ab,float)
    n = temp_matrix.shape[0]
    a = temp_matrix[:, :-1]
    b = temp_matrix[:, -1]

    for i in range(n):
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            a[j] = a[j] - factor * a[i]
            b[j] = b[j] - factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i][i + 1:], x[i + 1:])) / a[i][i]

    return x

def lu_decomposition(ab):
    temp_matrix = np.array(ab,float)
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


def gauss_jordan(A, b):
    A, b = np.array(A, dtype=float), np.array(b, dtype=float)
    n = len(A)
    aug = np.hstack([A.reshape(n, -1), b.reshape(n, 1)])
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(aug[i:, i]))
        aug[[i, max_row]] = aug[[max_row, i]]
        
        if abs(aug[i, i]) < 1e-10:
            return None
        
        aug[i] /= aug[i, i]
        for k in range(n):
            if k != i:
                aug[k] -= aug[k, i] * aug[i]
    
    return aug[:, -1]

def cramer_rule(A, b):
    A, b = np.array(A, dtype=float), np.array(b, dtype=float)
    n = len(A)
    det_A = np.linalg.det(A)
    
    if abs(det_A) < 1e-10:
        return None
    
    x = np.zeros(n)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        x[i] = np.linalg.det(Ai) / det_A
    
    return x
