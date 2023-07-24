from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" else Path.cwd()
cssfile = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "Ahmed Abdallah.pdf"
profile_pic = current_dir / "assets" / "av2.jpg"

page_title = "Ahmed's Resume"
name = "Ahmed Abdallah"
Description = "Fresh Data Analyst"
email = "ahmed.abdallah10024@gmail.com"
location = "Giza"
phone = "01141407873"
social_media = {
    "Linkedin": "https://www.linkedin.com/in/ahmed4abdallah4fever/",
    "GitHub": "https://github.com/ahmed-2001M",
}

PROJECTS = {
    "🏆 Scraping Bot - work to fetch durgs information from drugs.com": "https://github.com/ahmed-2001M/ScrapingBot",
    "🏆 CNN Model - for Lung Cancer Detection with Lung Segmentation": "https://github.com/ahmed-2001M/LungCancer-Model",
    "🏆 eCommerce Dataset - I was trying to get insights and do many types of segmentations": "https://github.com/ahmed-2001M/Play_wIth_DatA-/tree/master/ecommerce",
    "🏆 Drought dataset - I was trying to make this data ready for ML Models": "https://github.com/ahmed-2001M/mid-project",
}


st.set_page_config(page_title=page_title)


with open(cssfile) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    pdfbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


col1, col2 = st.columns([2, 4], gap="small")
with col1:
    st.image(
        profile_pic,
        use_column_width=True,
        output_format="JPEG",
        channels="RGB",
        clamp=False,
    )

with col2:
    st.title(name)
    st.write(Description)
    
    st.write("📫", email)
    st.write("🏙️",location)
    st.write("📞",phone)
    st.download_button(
        ":page_facing_up: Download Resume",
        data=pdfbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

st.write("#")

cols = st.columns(len(social_media))
for idx, (platform, link) in enumerate(social_media.items()):
    cols[idx].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """

- 👩‍💻 Programming Languages : (Python , c\c++, ease to learn any language )
- 📊 Data Science Skills : ( Data Cleaning, Data Analysis, Data Visualization, Web Scraping )
- 📚 CS Concepts : ( OOP, Problem Solving, Data Structures, Algorithms)
- 🗄️ Database : (SQL , Mysql )
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"- [{project}]({link})")