import sympy
from sympy import symbols, sympify, solve, Eq

from Functions import false_position,bi_section,simple_fixed_point
equ = "0.9*x**2+1.7*x+2.5"
print(simple_fixed_point(5,equ,1))
