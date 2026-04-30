import streamlit as st

st.set_page_config(page_title="Numerical Analyst", page_icon="📊")
url = "https://www.mti.edu.eg/"
st.title("Numerical Analyst")
st.write("a Mini project to solve linear algebraic equations and finding roots for polynomials.")
st.markdown("Built by CS & AI Students at [MTI university](%s)." % url)
st.header("Polynomials:")
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
st.header("Linear algebraic equations:")
st.subheader("Gauss elimination:")
st.markdown("<>The elimination of unknowns was used to solve a pair of" \
"simultaneous equations. The procedure consisted of two steps:1. The equations were manipulated to eliminate one of the" \
"unknowns from the equations. The result of this elimination" \
"step was that we had one equation with one unknown." \
"2. Consequently, this equation could be solved directly and the" \
"result back-substituted into one of the original equations to" \
"solve for the remaining unknown.This basic approach can be extended to large sets of equations by" \
"developing a systematic scheme or algorithm to eliminate unknownsand to back-substitute." \
" Gauss elimination is the most basic of these" \
"schemes.</small>",unsafe_allow_html=True)
st.subheader("LU decomposition:")
st.markdown("<small>\
            Gauss elimination is designed to solve systems of linear algebraic" \
            "equations,[𝐴]{𝑋} = {𝐵} (2.8)Although it certainly represents a sound way to solve such systems," \
            "it becomes inefficient when solving equations with the same" \
            "coefficients [A], but with different right-hand-side constants (theb’s)." \
            "Recall that Gauss elimination involves two steps: forward" \
            "elimination and back substitution. Of these, the forward-elimination" \
            "step comprises the bulk of the computational effort. This i" \
            "particularly true for large systems of equations." \
            "LU decomposition methods separate the time-consuming" \
            "elimination of the matrix [A] from the manipulations of the right-" \
            "hand side {B}. Thus, once [A] has been “decomposed,” multiple" \
            "right-hand-side vectors can be evaluated in an efficient manner." \
            "Interestingly, Gauss elimination itself can be expressed as an LU" \
            "decomposition. Before showing how this can be done, let us first" \
            "provide a mathematical overview of the decomposition strategy.</small>", unsafe_allow_html=True)
st.subheader("Cramer's Rule:")
st.markdown("<small>Cramer’s rule is another solution technique that is best suited to" 
            "small numbers of equations. Before describing this method, we will"
            "briefly introduce the concept of the determinant, which is used to"
            "implement Cramer’s rule. In addition, the determinant has relevance"
            "to the evaluation of the ill-conditioning of a matrix.</small>", unsafe_allow_html=True)
st.subheader("Gauss-Jordan method:")
st.markdown("<small>Gauss-Jordan elimination is a modification of Gauss elimination that" \
    "eliminates the need for back substitution. In Gauss elimination, the" \
    "forward-elimination step transforms the original system of equations" \
    "into an upper triangular form. The back-substitution step then" \
    "solves for the unknowns starting with the last equation and working" \
    "backward to the first. In contrast, Gauss-Jordan elimination" \
    "transforms the original system of equations into a diagonal form, so" \
    "that the solution can be read directly from the resulting equations." \
    "The Gauss-Jordan method is more computationally intensive than Gauss" \
    "elimination, but it is more straightforward to implement and can be" \
    "more efficient for small systems of equations.</small>", unsafe_allow_html=True)
