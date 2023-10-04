from pathlib import Path
import streamlit as st

# --- LOAD CSS --- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "technicalSkillsStyles.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- PAGE DESCRIPTION ---
st.header("More about the Technical Stuff...")
st.write("As a current Computer Science Student and an Aspiring Software Engineer, a combination of my Hard and Soft skills have been developed both in and out of the classroom.") 
st.write("Below are some of my current skills and focuses.") 

# --- PROGRAMMING LANGUAGES --- 
with st.container():
    col1, col2=st.columns(2, gap="small")
    
    with col1:
        st.subheader("Programming Languages") 
       
    with col2: 
        st.text("""
- Python 
    - JavaScript
        - C++
"""                
                )
st.empty()

 # --- SOFTSKILLS --- 
with st.container():
    col1, col2=st.columns(2, gap="small")

    with col1: 
        st.subheader("Soft Skills") 

    with col2:
        st.text("""
- Good Written and Oral Communication Skills 
    - Strong Organization and Time Management
        - Ability to Cooperate with Team and Management
"""
                )
        