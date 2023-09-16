from pathlib import Path
import streamlit as st

# --- LOAD CSS --- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "technicalSkillsStyles.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- PAGE DESCRIPTION ---
st.header("Technical Skills")
st.write("As a current Computer Science Student and an Aspiring Software Engineer, it is through the diversification and application of various skills that I can become an effective workforce canadite.")

# --- PROGRAMMING LANGUAGES --- 
with st.container():
    col1, col2=st.columns(2, gap="small")
    
    with col1:
        st.subheader("Programming Languages") 
       
    with col2: 
        st.text("""
- Python 
    - Java
        - C++
"""                
                )
st.empty()

 # --- ACADEMIC INTERESTS --- 
with st.container():
    col1, col2=st.columns(2, gap="small")

    with col1: 
        st.subheader("Academic Interests") 

    with col2:
        st.text("""
- Software Engineering
    - Data Science
        - Machine Learning 
"""
                )