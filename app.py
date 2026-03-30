from Functions import *
import streamlit as st
import pandas as pd


def display():
    df = pd.DataFrame({
        'xl' :[]
        'xu':
    })
    st.table()



st.title("NUMERICAL ANALYSIS")
st.write("----------------")
st.subheader("Choose a method to use:")


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Bisection", "False Position", "Newton's", "Secant", "Gauss", "L&U"])

with tab1:
        with st.form(key="my_form"):
            xl = st.number_input("xl :")
            xu = st.number_input("xu :")
            equ = st.text_input("Equation :")
            expected_error = st.number_input("Expected Error:")
            submit_button = st.form_submit_button("Submit")
            if submit_button:
              bi_section(xl,xu,equ,expected_error)
