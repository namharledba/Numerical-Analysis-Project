from Functions import *
import streamlit as st
st.header("Polynomials")
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Bisection", "False position", "Simple Fixed point",
    "Newton's method", "Secant"])
with tab1 :
    st.subheader("Bisection method:")
    st.markdown(
                "<small>The bisection method, which is alternatively called <u>binary chopping</u>, <u>interval halving</u>, or "
                "<u>Bolzano’s method</u>, is one type of incremental search method in which the interval is always divided in half."
                " If a function changes sign over an interval, the function value at the midpoint is evaluated. "
                "The location of the root is then determined as lying at the midpoint of the subinterval within which the sign change occurs."
                " The process is repeated to obtain refined estimates.</small>", unsafe_allow_html=True)
    st.write("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
    
    with st.form("Bisection method"): 
        
        xl = st.number_input("Enter xl", value=0.0)
        xu = st.number_input("Enter xu", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error")
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        
        if st.form_submit_button("Calculate"):

            if equ == "":
                st.error("Please enter the function f(x)")
                st.stop()
    
            is_valid_func, err_msg = validate_function(equ)
            if not is_valid_func:
                st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                st.stop()
            if not valid(xu, xl, equ):
                st.warning("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
                st.stop()
    
            if not valid_error(expected_error):
                st.warning("Expected error must be in range (0, 100)")
                st.stop()
    
            result = bi_section(xl, xu, equ, expected_error, int(max_iterations))
            if result is None:
                st.error("No result returned.")
                st.stop()
            else:
                st.success("result:")
                st.session_state["bisection_df"] = result
                st.session_state["bisection_row_index"] = 0
            
    if "bisection_df" in st.session_state:
            df = st.session_state["bisection_df"]
            row_index = st.session_state.get("bisection_row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "bisection_next_row"):
                            st.session_state["bisection_row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "bisection_show_all"):
                            st.session_state["bisection_row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")


with tab2 :
    
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
    
    with st.form("False position method"):
        
        xl = st.number_input("Enter xl", value=0.0)
        xu = st.number_input("Enter xu", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error")
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)

        if st.form_submit_button("Calculate"):

            if equ == "":
                st.error("Please enter the function f(x)")
                st.stop()
    
            is_valid_func, err_msg = validate_function(equ)
            if not is_valid_func:
                st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                st.stop()
    
            if not valid(xu, xl, equ):
                st.warning("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
                st.stop()
    
            if not valid_error(expected_error):
                st.warning("Expected error must be in range (0, 100)")
                st.stop()
    
            result = false_position(xl, xu, equ, expected_error, int(max_iterations))
            if result is None:
                st.error("No result returned.")
                st.stop()
            else:
                st.success("result:")
                st.session_state["false_position_df"] = result
                st.session_state["false_position_row_index"] = 0
            
    if "false_position_df" in st.session_state:
            df = st.session_state["false_position_df"]
            row_index = st.session_state.get("false_position_row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "false_position_next_row"):
                            st.session_state["false_position_row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "false_position_show_all"):
                            st.session_state["false_position_row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")


with tab3 :
    
    st.subheader("Simple fixed point method:")
    st.write("<small>Open methods employ a formula to predict the root. Such a" 
     "formula can be developed for simple fixed-point iteration (or, as it isalso called," 
     "one-point iteration or successive substitution) by" 
     "rearranging the function f (x) = 0 so that x is on the left-hand side ofthe equation x = g(x) , "
     "This transformation can be accomplished either by algebraic" \
     "manipulation or by simply adding x to both sides of the original" \
     "equation. For example,𝑥2 − 2𝑥 + 3 = 0 " \
     "can be simply manipulated to yield 𝑥 = (𝑥2 + 3)/2.</small>", unsafe_allow_html=True)

    with st.form("Simple fixed point method"):
        initial = st.number_input("Enter initial guess", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)

        if st.form_submit_button("Calculate"):

            if equ == "":
                st.error("Please enter the function f(x)")
                st.stop()
    
            is_valid_func, err_msg = validate_function(equ)
            if not is_valid_func:
                st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                st.stop()
    
            if not valid_error(expected_error):
                st.warning("Expected error must be in range (0, 100)")
                st.stop()
    
            result = simple_fixed_point(initial, equ, expected_error, int(max_iterations))
            if result is None:
                st.error("No result returned.")
                st.stop()
            else:
                st.success("result:")
                st.session_state["simple_fixed_point_df"] = result
                st.session_state["simple_fixed_point_row_index"] = 0
    
    if "simple_fixed_point_df" in st.session_state:
            df = st.session_state["simple_fixed_point_df"]
            row_index = st.session_state.get("simple_fixed_point_row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "simple_fixed_point_next_row"):
                            st.session_state["simple_fixed_point_row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "simple_fixed_point_show_all"):
                            st.session_state["simple_fixed_point_row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")


with tab4 :
    
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

    with st.form("Newton's method"):
        
        initial = st.number_input("Enter initial guess", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        if st.form_submit_button("Calculate"):
            if equ == "":
                st.error("Please enter the function f(x)")
                st.stop()
            is_valid_func, err_msg = validate_function(equ)
            if not is_valid_func:
                st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                st.stop()
            if not valid_error(expected_error):
                st.warning("Expected error must be in range (0, 100)")
                st.stop()

            result = newton_method(initial, equ, expected_error, int(max_iterations))
            
            if result is None:
                st.error("No result returned.")
                st.stop()
            else:
                st.success("result:")
                st.session_state["newton_df"] = result
                st.session_state["newton_row_index"] = 0
    
    if "newton_df" in st.session_state:
            df = st.session_state["newton_df"]
            row_index = st.session_state.get("newton_row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "newton_next_row"):
                            st.session_state["newton_row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "newton_show_all"):
                            st.session_state["newton_row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")


with tab5 :
    st.subheader("Secant method:")
    st.write("<small>A potential problem in implementing the Newton-Raphson" \
    "method is the evaluation of the derivative. Although this is not" \
    "inconvenient for polynomials and many other functions, there are" \
    "certain functions whose derivatives may be extremely difficult or" \
    "inconvenient to evaluate. For these cases, the derivative can be" \
    "approximated by a backward finite divided difference.</small>", unsafe_allow_html=True)

    with st.form("Secant method"):
        xi_1 = st.number_input("Enter xi-1", value=0.0)
        x0 = st.number_input("Enter x0", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        if st.form_submit_button("Calculate"):

            if equ == "":
                st.error("Please enter the function f(x)")
                st.stop()

            is_valid_func, err_msg = validate_function(equ)
            if not is_valid_func:
                st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                st.stop()

            elif not valid_error(expected_error):
                st.warning("Expected error must be in range (0, 100)")
                st.stop()

            result = se_cant(xi_1, x0, equ, expected_error, int(max_iterations))
            if result is None:
                st.error("No result returned.")
                st.stop()
            else:
                st.success("result:")
                st.session_state["secant_df"] = result
                st.session_state["secant_row_index"] = 0
    
    if "secant_df" in st.session_state:
            df = st.session_state["secant_df"]
            row_index = st.session_state.get("secant_row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "secant_next_row"):
                            st.session_state["secant_row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "secant_show_all"):
                            st.session_state["secant_row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")
