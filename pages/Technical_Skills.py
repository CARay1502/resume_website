import streamlit as st

st.header("Technical Skills")
st.write("As a current Computer Science Student and an Aspiring Software Engineer, it is through the diversification and application of various skills that I can become an effective workforce canadite.")

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