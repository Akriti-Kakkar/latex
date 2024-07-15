from termcolor import colored, cprint

import streamlit as st

import sys

text = colored("Latex Format", "green")
text1 = colored("new stuff", "red")

st.latex(text)

st.write(text)

st.html(text)

st.markdown(text)

st.write(f"${{text}}$", f"${{text1}}$")

st.button(f''':red[${{text}}$]
          
          :blue[${{text1}}$]''')

st.write(r"${}$".format(text))

st.write(r"""{}
         
         {}""".format(text, text1))

st.code(text)
