from Functions import *
import streamlit as st


def polynomials():
    st.session_state.option = 1

def linearalgebra():
    st.session_state.option = 2


if "option" not in st.session_state:
    st.session_state.option = 0


if st.session_state.option == 0:
        url = "https://www.mti.edu.eg/"
        st.title("Numerical Analyst")
        st.write("a Mini project to solve linear algebraic equations and finding roots for polynomials.")
        st.markdown("Built by CS & AI Students at [MTI university](%s)." % url)
        st.write("-----------------")
        col1, col2 = st.columns(2)
        with col1 :
            if st.button("Polynomials"):
                polynomials()
                st.rerun()
        with col2 :
            if st.button("Linear Algebraic Equations"):
                linearalgebra()
                st.rerun( )
elif st.session_state.option == 1:
        st.header("Polynomials")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Bisection", "False position", "Simple Fixed point", "Secant",
            "Newton's method"])
        if st.button("previous"):
            st.session_state.option = 0
            st.rerun()
        with tab1 :
            st.subheader("Bisection method:")
            st.markdown(
                "<small>The bisection method, which is alternatively called <u>binary chopping</u>, <u>interval halving</u>, or "
                "<u>Bolzano’s method</u>, is one type of incremental search method in which the interval is always divided in half."
                " If a function changes sign over an interval, the function value at the midpoint is evaluated. "
                "The location of the root is then determined as lying at the midpoint of the subinterval within which the sign change occurs."
                " The process is repeated to obtain refined estimates.</small>", unsafe_allow_html=True)
            st.write("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")

            with st.form("Bisection"):
                xl = st.number_input("Enter xl")
                xu = st.number_input("Enter xu")
                equ = st.text_input("Enter equation f(x)")
                expected_error = st.number_input("Enter expected error")
                if st.form_submit_button("Submit"):
                    result = bi_section(xl, xu, equ, expected_error)
                    st.table(result)


        with tab2 :
            st.subheader("False position method:")
            st.write("")
        with tab3 :
            st.subheader("Simple Fixed point method:")
            st.write("")
        with tab4 :
            st.subheader("Secant method:")
            st.write("")
        with tab5 :
            st.subheader("Newton's method:")
            st.write("")
elif st.session_state.option == 2:
        st.header("Linear Algebraic Equations")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Gauss Elimination","LU Decomposition","Cramer's Rule","Gauss-jorden Elimination"])
        if st.button("previous"):
            st.session_state.option = 0
            st.rerun()
        with tab1 :
            st.subheader("Gauss Elimination:")
            st.write("")
        with tab2 :
            st.subheader("LU Decomposition:")
            st.write("")
        with tab3 :
            st.subheader("Cramer's Rule:")
            st.write("")
        with tab4 :
            st.subheader("Gauss-jorden Elimination:")
            st.write("")
