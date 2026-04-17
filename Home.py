import streamlit as st

st.set_page_config(page_title="Numerical Analyst", page_icon="📊")
url = "https://www.mti.edu.eg/"
st.title("Numerical Analyst")
st.write("a Mini project to solve linear algebraic equations and finding roots for polynomials.")
st.markdown("Built by CS & AI Students at [MTI university](%s)." % url)

st.subheader("Bisection method:")
st.markdown(
                "<small>The bisection method, which is alternatively called <u>binary chopping</u>, <u>interval halving</u>, or "
                "<u>Bolzano’s method</u>, is one type of incremental search method in which the interval is always divided in half."
                " If a function changes sign over an interval, the function value at the midpoint is evaluated. "
                "The location of the root is then determined as lying at the midpoint of the subinterval within which the sign change occurs."
                " The process is repeated to obtain refined estimates.</small>", unsafe_allow_html=True)
st.write("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
st.subheader("False position method:")
st.write("<small>Although bisection is a perfectly valid technique for"
                     "determining roots, its “brute-force” approach is relatively"
                     "inefficient. False position is an alternative based on a graphical"
                     "insight. A shortcoming of the bisection method is that, in dividing"
                     "the interval from xl to xu into equal halves, no account is taken of"
                     "the magnitudes of f (xl) and f (xu). For example, if f (xl) is much"
                     "closer to zero than f (xu), it is likely that the root is closer to xl than to xu The fact that the replacement of the curve by a straight line"
                     "gives a “false position” of the root is the origin of the name, method"
                     "of false position, or in Latin, <u>regula falsi</u>. It is also called the <u>linear interpolation method</u>.</small>", unsafe_allow_html=True)
st.write("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
st.subheader("Simple fixed point method:")
st.write("<small>Open methods employ a formula to predict the root. Such a" 
     "formula can be developed for simple fixed-point iteration (or, as it isalso called," 
     "one-point iteration or successive substitution) by" 
     "rearranging the function f (x) = 0 so that x is on the left-hand side ofthe equation x = g(x) , "
     "This transformation can be accomplished either by algebraic" \
     "manipulation or by simply adding x to both sides of the original" \
     "equation. For example,𝑥2 − 2𝑥 + 3 = 0 " \
     "can be simply manipulated to yield 𝑥 = (𝑥2 + 3)/2.</small>", unsafe_allow_html=True)
st.subheader("Newton's method:")
st.write("<small>Perhaps the most widely used of all root-locating formulas is" \
    "the Newton Raphson equation,  If the initial guess at the" \
    "root is xi, a tangent can be extended from the point [xi, f(xi)]. The" \
    "point where this tangent crosses the x axis usually represents animproved estimate of the root." \
    "The Newton-Raphson method can be derived on the basis of the" \
    "geometrical interpretation, the first derivative at x isequivalent to the slope:"
    "𝑓′(𝑥𝑖) = (𝑓(𝑥𝑖) − 0 / 𝑥𝑖 − 𝑥𝑖+1)"
    "which can be rearranged to yield"
    "𝑥𝑖+1 = 𝑥𝑖 − (𝑓(𝑥𝑖)/𝑓′(𝑥𝑖))"
    "which is called the Newton-Raphson formula</small>", unsafe_allow_html=True)
st.subheader("Secant method:")
st.write("<small>A potential problem in implementing the Newton-Raphson" \
    "method is the evaluation of the derivative. Although this is not" \
    "inconvenient for polynomials and many other functions, there are" \
    "certain functions whose derivatives may be extremely difficult or" \
    "inconvenient to evaluate. For these cases, the derivative can be" \
    "approximated by a backward finite divided difference.</small>", unsafe_allow_html=True)
