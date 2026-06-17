import streamlit as st
import requests 
st. title('Projeto Harry Potter ')
st.sidebar.image('logo.png')

url  = "https://hp-api.onrender.com/api/characters"

resposta = requests.get(url)
dados = resposta.json()

nomes = []
for personagem in dados:
    nomes.append(personagem['name'])
nomes.sort()

nome_escolhido = st.sidebar.selectbox('Selecione:', nomes)

for p in dados:
    if p['name'] == nome_escolhido:
        personagem = p
        break  

st.header(personagem['name'])

if personagem ['image'] and personagem ['image'] != "":
    st.image(personagem['image'], width=300)
else:
    st.write("📸 Este personagem não possui imagem") 

st.divider()    

st.write(f"**casa:**{personagem['house']}")
st.write(f"**especie:** {personagem['species']}")
st.write(f"**genero:** {personagem['gender']}")
st.write(f'**Data de Nascimento:** {personagem['dateOfBirth']}')
st.write(f'**Ano de Nascimento:** {personagem['yearOfBirth']}')

st.write("**Varinha:**")

st.write("**Varinha:**")
st.write(f'- Madeira: {personagem['wand']['wood']}')
st.write(f'- Núcleo: {personagem['wand']['core']}')
st.write(f'- Tamanho: {personagem['wand']['length']} polegadas ')

st.write(f'**Patrono:** {personagem['patronus']}')
st.write(f'**Ator/Atriz:** {personagem['actor']}')

if personagem['alive']:
    st.write(f'**Está vivo?**Sim')
else:
    st.write(f'**Está vivo?**Não') 

