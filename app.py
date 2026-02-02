# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st
import pandas as pd
import numpy as np


# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# --- Page Config ---
st.set_page_config(page_title="Charles Tonongei - Research Profile", 
                   page_icon="📊", 
                   layout="wide")
st.write("\U0001F4CA Statistical Evaluation")

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Charles Tonongei"
    field = "Chemistry"
    institution = "University of Johannesburg"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

# --- Header --- 
st.subheader("Researcher in Statistical Evaluation")

st.write(""" 
Welcome to my research profile page. 
I specialize in **statistical evaluation**, focusing on data-driven insights, 
evaluation methodologies, and applied statistics for real-world problems. 
""")

# --- About Section --- 
st.header("👨‍🎓 About Me") 
st.write("""
I am passionate about applying statistical methods to evaluate programs, 
policies, and interventions. My work bridges theory and practice, ensuring
that statistical evaluation contributes to evidence-based decision-making.
""")


# --- Research Interests --- 
st.header("🔬 Research Interests") 
st.markdown(""" 
- Program evaluation using statistical methods 
- Impact assessment and causal inference 
- Survey design and data collection 
- Applied regression and predictive modeling 
- Statistical software development (R, Python, Stata) 
""")

# --- Publications / Projects ---
st.header("📚 Selected Work")
st.write("Here are some highlights of my research and projects:")

st.markdown(""" 
1. [Variographic analysis of a concentrator plant feed slurry stream data before and after intermediate hopper replacement](https://www.saimm.org.za/Conferences/files/wcsb11-2024/15_WCSB679-Tonongei.pdf) – Variography.
""")

# --- Contact Section --- 
st.header("📬 Contact") 

st.write("Feel free to reach out for collaboration or inquiries:") 

st.markdown("""
- **Email:** charles.tonongei@gmail.com
- **LinkedIn:** [linkedin.com/in/charlestonongei](https://linkedin.com) 
- **GitHub:** [github.com/charlestonongei](https://github.com)
""")

# --- Sidebar --- 
st.sidebar.success("Navigate using the sections above.")