from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw, ImageOps


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Christian Ray | Resume"
PAGE_ICON = ":wave:"
NAME = "Christian Ray"
DESCRIPTION = """
CS Student | Aspiring Software Engineer
"""
EMAIL = "christianray1502@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/christianray1502/",
    "LinkedIn": "https://www.linkedin.com/in/christian-ray-3695a8287/",
    "GitHub": "https://github.com/CARay1502",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC --- 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
import streamlit as st

# --- Business Card --- #
# --- ORIGINAL BUISNESS CARD INFO --- 
with st.container():
    col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2: 
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL MEDIA LINKS --- 
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.divider()

# --- HARD SKILLS --- 
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- Programming: Python, SQL, JavaScript, C
- Web Development: Django, Swift, Steamlit (This portfolio is Streamlit!)
    """
)

st.write('\n')
st.subheader("Education") 
st.write(
    """
- Graduated Elementary School
- Graduated Middle School
- Graduated High School 
- Graduated Gaston College  (*expected*)
- Gradiuated University of North Carolina At Charlotte  (*expected*)
"""
)
st.write('\n') 
st.subheader("Work History")
st.write(
    """
- Website Manager at Indiana Bible College"""

)
st.caption(
    """
    - - Assisted in Data Collection/Publishing, Front-End & Back-End Work.
    """
)
