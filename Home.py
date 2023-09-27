import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Images/photo.jpg")

with col2:
    st.title("Francisco Corte-Real")
    content = """
    Desde 2000 que estou envolvido em produção multímédia e informática
     a diversos níveis, começando como técnico de som em eventos,
      até à programação em várias línguagens, passando pela fotografia,
       vídeo, web design, etc...
          Por razões pessoais fui mantendo
         durante os últimos anos a profissão de vigilante à medida que fui
          realizando trabalhos como freelancer. Após algumas formações na área
           de multimédia, em 2006/2007 ingressei no curso de Novas Tecnologias
            da Comunicação na UA, tendo, infelizmente, concluído apenas pouco
             mais de metade do curso. 
             A nível de software, para além de conhecimentos
              em toda a gama Adobe, tenho também conhecimentos em alguns dos software’s
               gratuitos existentes, assim como software’s de CAD, 2D e 3D, e também
                algumas linguagens de programação. Neste momento procuro trabalho full-time,
                 tendo me dedicado nos últimos tempos a estudar a linguagem Python
                  e a sua integração em bases dados SQL e API’s, conhecer as suas principais
                   frameworks e tools assim como a integração dos mesmos.
    
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
        st.image("Images/" + row["image"])
        st.write(f"[Link for app]({row['url']})")
        st.write(f"[Github repository]({row['github']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Link for app]({row['url']})")
        st.write(f"[Github repository]({row['github']})")