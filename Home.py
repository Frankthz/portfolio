import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Francisco Corte-Real")
    content = """
    Since 2000, I have been involved in multimedia and IT 
    production at different levels, starting as a sound 
    technician at events, to programming in several languages, 
    including photography, video, web design, etc... 
    For personal reasons I have maintained over the last 
    few years in the security profession as I carried out 
    freelance work. After some training in the multimedia 
    area, in 2006/2007 I joined the New Communication Technologies 
    course at UA, having, unfortunately, only completed just over 
    half of the course. In terms of software, in addition to 
    knowledge of the entire Adobe range, I also have knowledge 
    of some of the free software available, as well as CAD, 
    2D and 3D software, and also some programming languages. 
    At the moment I am looking for a full-time job, having recently 
    dedicated myself to studying the Python language and its 
    integration into SQL databases and APIs, getting to know 
    its main frameworks and tools as well as their integration.
    
    """
    st.info(content)


info1 = ("Below you can find some of the apps I have built in Python trought some tutorials I have made. "
         "Some of the apps or code doesn't have web app, but you can check the code on 'GitHub'. Feel free to contact me.")
info2 = ("Unfourtanlly some of the apps haven't been added yet.")

st.info(info1)
st.info(info2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Link for app]({row['url']})")
        st.write(f"[Github repository]({row['github']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Link for app]({row['url']})")
        st.write(f"[Github repository]({row['github']})")