from Functions import *
import streamlit as st
st.header("Polynomials")
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Bisection", "False position", "Simple Fixed point",
    "Newton's method", "Secant"])
with tab1 :  
    with st.form("Bisection method"): 
        st.header("Bisection method")

        xl = st.number_input("Enter xl", value=0.0)
        xu = st.number_input("Enter xu", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error")
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        
        if st.form_submit_button("Calculate"):

            error_found = False

            if equ == "":
                st.error("Please enter the function f(x)")
                error_found = True
    
            is_valid_func, err_msg = validate_function(equ)
            
            if not error_found:
                
                if not is_valid_func:
                    st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                    error_found = True

            if not error_found:
                if not valid(xu, xl, equ):
                    st.warning("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
                    error_found = True

            if not error_found:    
                if not valid_error(expected_error):
                    st.warning("Expected error must be in range (0, 100)")
                    error_found = True
            if not error_found:
                result = bi_section(xl, xu, equ, expected_error, int(max_iterations))
                if result is None:
                    st.error("No result returned.")
                    error_found = True
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

    if st.button("Round", key="bisection_round"):
        st.write("Rounded values:")
        df_display = df.copy()
        df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
        df_display = df_display.round(3)
        df_display['Error'] = df_display['Error'].fillna('---')

        st.write(df_display)


with tab2 :
    
    with st.form("False position method"):
        st.header("False position method")

        xl = st.number_input("Enter xl", value=0.0)
        xu = st.number_input("Enter xu", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error")
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)

        if st.form_submit_button("Calculate"):
            error_found = False
            
            if not error_found:
                if equ == "":
                    st.error("Please enter the function f(x)")
                    error_found = True
    
            is_valid_func, err_msg = validate_function(equ)
            
            if not error_found:
                if not is_valid_func:
                    st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                    error_found = True
            
            if not error_found:
                if not valid(xu, xl, equ):
                    st.warning("Make sure that f(x) is real and continuous in the interval from xl to xu and f(xl) and f(xu) have opposite signs")
                    error_found = True

            if not error_found:
                if not valid_error(expected_error):
                    st.warning("Expected error must be in range (0, 100)")
                    error_found = True
    
            if not error_found:
                result = false_position(xl, xu, equ, expected_error, int(max_iterations))
                if result is None:
                    st.error("No result returned.")
                    error_found = True
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

    if st.button("Round", key="false_position_round"):
        st.write("Rounded values:")
        df_display = df.copy()
        df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
        df_display = df_display.round(3)
        df_display['Error'] = df_display['Error'].fillna('---')

        st.write(df_display)


with tab3 :

    with st.form("Simple fixed point method"):
        st.header("Simple fixed point method")

        initial = st.number_input("Enter initial guess", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)

        if st.form_submit_button("Calculate"):
            error_found = False
            if not error_found:
                if equ == "":
                    st.error("Please enter the function f(x)")
                    error_found = True
            
            is_valid_func, err_msg = validate_function(equ)
            
            if not error_found:
                if not is_valid_func:
                    st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                    error_found = True
            
            if not error_found:
                if not valid_error(expected_error):
                    st.warning("Expected error must be in range (0, 100)")
                    error_found = True

            if not error_found:
                result = simple_fixed_point(initial, equ, expected_error, int(max_iterations))
                if result is None:
                    st.error("No result returned.")
                    error_found = True
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

    if st.button("Round", key="simple_fixed_point_round"):
        st.write("Rounded values:")
        df_display = df.copy()
        df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
        df_display = df_display.round(3)
        df_display['Error'] = df_display['Error'].fillna('---')

        st.write(df_display)


with tab4 :

    with st.form("Newton's method"):
        st.header("Newton's method")
        
        initial = st.number_input("Enter initial guess", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        
        if st.form_submit_button("Calculate"):
            error_found = False
            if not error_found:
                if equ == "":
                    st.error("Please enter the function f(x)")
                    error_found = True
            
            if not error_found:
                is_valid_func, err_msg = validate_function(equ)
                if not is_valid_func:
                    st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                    error_found = True
            
            if not error_found:
                if not valid_error(expected_error):
                    st.warning("Expected error must be in range (0, 100)")
                    error_found = True

            if not error_found:
                result = newton_method(initial, equ, expected_error, int(max_iterations))
                if result is None:
                    st.error("No result returned.")
                    error_found = True
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

    if st.button("Round", key="newton_round"):
        st.write("Rounded values:")
        df_display = df.copy()
        df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
        df_display = df_display.round(3)
        df_display['Error'] = df_display['Error'].fillna('---')

        st.write(df_display)


with tab5 :

    with st.form("Secant method"):
        st.header("Secant method")

        xi_1 = st.number_input("Enter xi-1", value=0.0)
        x0 = st.number_input("Enter x0", value=0.0)
        equ = st.text_input("Enter the function f(x)", value="")
        expected_error = st.number_input("Enter the expected error", value=0.0)
        max_iterations = st.number_input("Enter the maximum number of iterations", value=0)
        
        if st.form_submit_button("Calculate"):
            error_found = False
            if not error_found:
                if equ == "":
                    st.error("Please enter the function f(x)")
                    error_found = True

            if not error_found:
                is_valid_func, err_msg = validate_function(equ)
                if not is_valid_func:
                    st.error("Invalid function: please use proper math syntax (e.g. x**2 - 4, sin(x))")
                    error_found = True

            if not error_found:
                if not valid_error(expected_error):
                    st.warning("Expected error must be in range (0, 100)")
                    error_found = True

            if not error_found:
                result = se_cant(xi_1, x0, equ, expected_error, int(max_iterations))
                if result is None:
                    st.error("No result returned.")
                    error_found = True
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

    if st.button("Round",key= "secant_round"):
        st.write("Rounded values:")
        df_display = df.copy()
        df_display['Error'] = pd.to_numeric(df_display['Error'], errors='coerce')
        df_display = df_display.round(3)
        df_display['Error'] = df_display['Error'].fillna('---')

        st.write(df_display)
