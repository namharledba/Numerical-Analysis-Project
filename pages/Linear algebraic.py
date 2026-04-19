from Functions import *
import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Gauss elimination", "LU decomposition", 
                                        "Cramer's Rule", "Gauss-Jordan method"])

with tab1:
    
    with st.form("Gauss elimination"):
        st.header("Gauss elimination")
        st.write("Enter the augmented matrix (A|b) row by row, separating values with spaces:")
        
        matrix_input = st.text_area("Augmented Matrix (A|b)", height=200)
        submit_button = st.form_submit_button("Solve")
        if submit_button:
                matrix = [list(map(float, row.split())) for row in matrix_input.strip().split('\n')]
                solution = gauss_elimination(matrix)
                for i in range(len(solution)):
                    st.write(f"x{i+1} = {solution[i]}")

with tab2:
    
    with st.form("LU decomposition"):
        st.header("LU decomposition")
        st.write("Enter the augmented matrix (A|b) row by row, separating values with spaces:")
        
        matrix_input = st.text_area("Augmented Matrix (A|b)", height=200)
        submit_button = st.form_submit_button("Solve")
        if submit_button:
                matrix = [list(map(float, row.split())) for row in matrix_input.strip().split('\n')]
                solution = lu_decomposition(matrix)
                for i in range(len(solution)):
                    st.write(f"x{i+1} = {solution[i]}")

with tab3:
    st.header("Cramer's Rule")

with tab4:
    st.header("Gauss-Jordan method")
