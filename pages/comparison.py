from Functions import *
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparison Center", layout="wide")

st.title(" Methods Comparison Center")
st.write("Compare different numerical methods side-by-side.")

main_tab1, main_tab2 = st.tabs(["Linear Algebra Comparison", "Polynomials Comparison"])

with main_tab1:
    st.header("Linear Systems (A|b)")
    with st.form("algebra_comparison"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Method 1")
            alg_m1 = st.selectbox("Select Method", ["Gauss elimination", "LU decomposition", "Cramer's Rule", "Gauss-Jordan"], key="alg1")
            a1_input = st.text_area("Matrix (A)", height=150, key="a1")
            b1_input = st.text_area("Vector (b)", height=100, key="b1")
            
        with col2:
            st.subheader("Method 2")
            alg_m2 = st.selectbox("Select Method", ["Gauss-Jordan", "Gauss elimination", "LU decomposition", "Cramer's Rule"], key="alg2")
            a2_input = st.text_area("Matrix (A2)", height=150, key="a2")
            b2_input = st.text_area("Vector (b2)", height=100, key="b2")
            
        submit_alg = st.form_submit_button("Compare Algebra Methods")

    if submit_alg:
        try:
            def solve_alg(method, a_txt, b_txt):
                A = [list(map(float, row.split())) for row in a_txt.strip().split('\n')]
                b = [float(val) for val in b_txt.strip().split()]
                if method == "Gauss elimination" or method == "LU decomposition":
                    aug = [A[i] + [b[i]] for i in range(len(A))]
                    return gauss_elimination(aug) if method == "Gauss elimination" else lu_decomposition(aug)
                return cramer_rule(A, b) if method == "Cramer's Rule" else gauss_jordan(A, b)

            res1 = solve_alg(alg_m1, a1_input, b1_input)
            res2 = solve_alg(alg_m2, a2_input, b2_input)

            out1, out2 = st.columns(2)
            with out1:
                st.success(f"Result ({alg_m1})")
                for i in range(len(res1)): st.write(f"x{i+1} = {res1[i]}")
            with out2:
                st.success(f"Result ({alg_m2})")
                for i in range(len(res2)): st.write(f"x{i+1} = {res2[i]}")
        except Exception as e:
            st.error(f"Algebra Error: {e}")

with main_tab2:
    st.header("Polynomial Roots Comparison")
    with st.form("poly_comparison"):
        equ = st.text_input("Enter the function f(x)", value="x**2 - 4")
        expected_error = st.number_input("Expected Error", value=0.001, format="%.4f")
        max_iterations = st.number_input("Max Iterations", value=10)
        
        st.divider()
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            st.subheader("Method 1 Settings")
            p_m1 = st.selectbox("Select Method", ["Bisection", "False position", "Simple Fixed point", "Newton's method", "Secant"], key="pm1")
            p1_val1 = st.number_input("Initial Guess 1 / xl", value=0.0, key="p1v1")
            p1_val2 = st.number_input("Initial Guess 2 / xu", value=3.0, key="p1v2")
            
        with col_p2:
            st.subheader("Method 2 Settings")
            p_m2 = st.selectbox("Select Method", ["Newton's method", "Bisection", "False position", "Simple Fixed point", "Secant"], key="pm2")
            p2_val1 = st.number_input("Initial Guess 1 / xl", value=0.0, key="p2v1")
            p2_val2 = st.number_input("Initial Guess 2 / xu", value=3.0, key="p2v2")
            
        submit_poly = st.form_submit_button("Compare Polynomial Methods")

    if submit_poly:
        try:
            def solve_poly(method, v1, v2, eq, err, iters):
                if method == "Bisection": return bi_section(v1, v2, eq, err, iters)
                if method == "False position": return false_position(v1, v2, eq, err, iters)
                if method == "Simple Fixed point": return simple_fixed_point(v1, eq, err, iters)
                if method == "Newton's method": return newton_method(v1, eq, err, iters)
                if method == "Secant": return se_cant(v1, v2, eq, err, iters)

            df1 = solve_poly(p_m1, p1_val1, p1_val2, equ, expected_error, int(max_iterations))
            df2 = solve_poly(p_m2, p2_val1, p2_val2, equ, expected_error, int(max_iterations))

            out_p1, out_p2 = st.columns(2)
            with out_p1:
                st.success(f"{p_m1} Iterations")
                df_display = df1.copy()
                df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
                df_display = df_display.round(3)
                df_display['Error'] = df_display['Error'].fillna('---')
                st.write(df_display)

            with out_p2:
                st.success(f"{p_m2} Iterations")
                df_display = df2.copy()
                df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
                df_display = df_display.round(3)
                df_display['Error'] = df_display['Error'].fillna('---')
                st.write(df_display)
        except Exception as e:
            st.error(f"Polynomial Error: {e}")
