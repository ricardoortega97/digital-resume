from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title = "My webpage", page_icon= ":tada", layout= "wide")

def load_lottieUrl(url):
    r = requests.get(url)
    if r.status_code != 200: #If request works, it will return a data score of 200 else returns none
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Load Assits---
lottie_coding = load_lottieUrl("https://lottie.host/fecdb962-b4d0-417d-a86c-c3eb2d7dde03/ddXqoGz3Ej.json")
img_discord = Image.open("images/header.png")



#--- Hader Section
st.subheader("Hi, I am Ricardo ")
st.title("An App dev From ATL ")
st.write(" I am Currently a seinor at GSU pursing CIS as an Application Dev! ")
#st.write("[Learn More >]")

#----What to do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do.")
        st.write("##")
        st.write("""
        I Am a GSU student looking for an internship to hone my skills in:
        - Python (Pycharm)
        - Java (Eciplse)
         Data Visualization:
        - Microsoft Excel 
        """)
    with right_column:
        st_lottie(lottie_coding, height= 300,key="coding" )

#installing lottie files to add animation or pictures


#---Projects---
with st.container():
    st.write("---")
    st.header("My Projects:")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_discord)
    with text_column:
        st.subheader("Discord bot:")
        st.write("""
        Learned how to implement a bot in discrd with python. 
        During the progress of settng up a discord bot, You had to create a token to use this bot. 
        While setting up the project, there was some difficuilties as the reference was outdated, so i
        had to look for information with the new dated reference. Intents was not needed and was the main issue 
        that prevent my code not to run and cause an error. 
        """)


#---Conatact---
with st.container():
    st.write("---")
    st.header("How to get in touch with me:")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ricardo.ortega97@outlook.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder= "Your Email" required>
     <textarea name="message" placeholder="Your Message Here." required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()