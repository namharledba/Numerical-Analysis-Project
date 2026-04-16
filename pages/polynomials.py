from Functions import *
import streamlit as st
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
                st.session_state["df"] = result
                st.session_state["row_index"] = 0
            
    if "df" in st.session_state:
            df = st.session_state["df"]
            row_index = st.session_state.get("row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "bisection_next_row"):
                            st.session_state["row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "bisection_show_all"):
                            st.session_state["row_index"] = len(df) - 1
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
                st.session_state["df"] = result
                st.session_state["row_index"] = 0
            
    if "df" in st.session_state:
            df = st.session_state["df"]
            row_index = st.session_state.get("row_index", 0)
            st.dataframe(df.iloc[: row_index + 1])
            if row_index < len(df) - 1:
                col1, col2 = st.columns([1, 1])

                with col1:
                        if st.button("Next Row",key = "false_position_next_row"):
                            st.session_state["row_index"] += 1
                            st.rerun()

                with col2:
                        if st.button("Show All",key = "false_position_show_all"):
                            st.session_state["row_index"] = len(df) - 1
                            st.rerun()
            else:
                    st.info("All rows displayed.")


with tab3 :
     st.subheader("Simple fixed point method:")
