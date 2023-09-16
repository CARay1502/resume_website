from pathlib import Path
import streamlit as st
import time
from PIL import Image, ImageDraw, ImageOps
from streamlit_lottie import st_lottie


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume_updated.pdf"
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

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- NAV BAR ---

# --- LOAD CSS, PDF & PROFILE PIC --- 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Business Card --- 
with st.container():
    col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2: 
    st.title(NAME)
    st.write(DESCRIPTION)
    if st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        use_container_width=True,
    ):
        st.toast('Yay!')
        time.sleep(.5) 
        st.toast('Thank you for checking out my Resume!', icon='🎉') 

    # --- Experiemental Email Button --- 
    def create_mailto_link(email):
        return f"mailto:{email}"
    
    if st.button(
        label="christianray1502@gmail.com",
                 use_container_width=True):
        mailto_link = create_mailto_link(EMAIL) 
        st.write(f"Click [here]({mailto_link}) to email me.") 

# --- SOCIAL MEDIA LINKS --- 
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.divider()

# --- EXperiemental Social Media Icons ---

# --- ABOUT ME --- 
st.write('\n')
st.subheader("A little bit about me...")
st.write("""
😁 Hi, my name is Christian! I am an aspiring Software Engineer based in Charlotte. Having previous experience building and deploying web applications, I am seeking unique internships to both grow my experience and broaden my knowledge of the tech field before embarking on my software career upon graduation. 
"""
)
st.write("""
🧑‍🎓 Both my academic background and future path are centered around Computer Science. I first attended Indiana Bible College, where I recieved my Associate degree in Christian Leadership. I am currently pursuing my Associate of Science through Gaston College with future plans to attend UNC Charlotte to a Bachelors degree in Computer Science. Along with multiple certifications and various coursework, I have built a repetoire for a prospective Software Engineer.
"""
)
st.write(
    """
🎯 I have several different hobbies and passions. 🏋️‍♂️ I like to workout at the gym. 🚗 I LOVE cars, both driving and admiring. 💻 I also love Coding, I have several different ideas/projects that I'm always working on!
"""
)

st.caption(
    """
Click on the navigation menu on the left to learn more!
"""
)