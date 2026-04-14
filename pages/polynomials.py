import streamlit as s

st.header("Polynomials")
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Bisection", "False position", "Simple Fixed point", "Secant",
    "Newton's method"])
with tab1 :
    st.subheader("Bisection method:")
    st.markdown(
                "<small>The bisection method, which is alternatively called <u>binary chopping</u>, <u>interval halving</u>, or "
                "<u>Bolzano’s method</u>, is one type of incremental search method in which the interval is always divided in half."
                " If a function changes sign over an interval, the function value at the midpoint is evaluated. "
                "The location of the root is then determined as lying at the midpoint of the subinterval within which the sign change occurs."
                " The process is repeated to obtain refined estimates.</small>", unsafe_allow_html=True)
    st.write("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
