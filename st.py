from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" else Path.cwd()
cssfile = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "Ahmed Abdallah.pdf"
profile_pic = current_dir / "assets" / "av2.jpg"

print(cssfile)

page_title = "Ahmed's Resume"
page_icon = "✋"
name = "Ahmed Abdallah"
Description = "Fresh Data Analyst"
email = "ahmed.abdallah10024@gmail.com"
social_media = {
    "Linkedin": "https://www.linkedin.com/in/ahmed4abdallah4fever/",
    "GitHub": "https://github.com/ahmed-2001M",
    }

st.set_page_config(page_title=page_title, page_icon="✋")





with open(resume_file, "rb") as pdf_file:
    pdfbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


col1, col2 = st.columns([2,4], gap="small")
with col1:
    st.image(
        profile_pic,
        use_column_width=True,
        output_format="JPEG",
        channels="RGB",
        caption="Profile Picture",
        clamp=False,
        width=150,
        )
    # st.markdown("<style>img{width:150px}</style>", unsafe_allow_html = True)

with col2:
    st.title(name)
    st.write(Description)
    st.download_button(
        ":page_facing_up: Download Resume",
        data=pdfbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)
    
    
    
st.write("#")
cols = st.columns(len(social_media))
for idx,(platform, link) in enumerate(social_media.items()):
    cols[idx].write(f"[{platform}]({link})")




with open(cssfile) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)