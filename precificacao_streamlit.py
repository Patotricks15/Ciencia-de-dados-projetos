import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, PolynomialFeatures, StandardScaler, MaxAbsScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import streamlit as st

df = pd.read_csv('Desafio2_input.csv', sep=';')

X = df[['Zona', 'Area', 'Qualidade', 'AnoConstrucao', 'QualidadeAquecimento', 'Banheiros', 'Comodos', 'Lareiras',
        'Garagem']]
Y = df['Preco']

X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=True)

label_X = LabelEncoder()
X_treino['Zona'] = label_X.fit_transform(X_treino['Zona'])
X_teste['Zona'] = label_X.fit_transform(X_teste['Zona'])
X_teste['QualidadeAquecimento'] = label_X.fit_transform(X_teste['QualidadeAquecimento'])
X_treino['QualidadeAquecimento'] = label_X.fit_transform(X_treino['QualidadeAquecimento'])

lr = LinearRegression(normalize=True)
lr.fit(X_treino, Y_treino)
previsao = lr.predict(X_teste)
resid = Y_teste - previsao

st.title('Resolução do desafio - KeyCash')
st.markdown('# Precificação de imóveis')
st.markdown('## Selecione os valores e o algoritmo definirá um preço para o imóvel')
st.markdown('''### Descrição das variáveis:
* **Zona:** Classificação da zona de venda

    0 - Zona de baixa densidade
    
    1 - Zona de alta densidade
    
* **Área:** Área em pés quadrados

* **Qualidade:** Qualidade do material e acabamento do imóvel

* **Ano:**

* **Qualidade do aquecimento:**

    0: Excelente
    
    1: Bom
    
    2: Mediano
    
    3: Aceitável

* **Banheiros:** Quantidade de banheiros

* **Cômodos:** Quantidade de cômodos

* **Lareiras:** Quantidade de lareiras

* **Garagem:** Tamanho da garagem em termos de quantidade de carros''')

zona = st.selectbox('Zona', [0, 1])
area = st.slider('Área', 1000, 20000)
qualidade = st.selectbox('Qualidade', [4, 5, 6, 7, 8])
ano = st.slider('Ano de construção', 1940, 2010)
quali_aque = st.selectbox('Aquecimento', [0, 1, 2, 3])
banheiros = st.selectbox('Banheiros', [1, 2])
comodos = st.selectbox('Comodos', [3, 4, 5, 6, 7, 8])
lareiras = st.selectbox('Lareiras', [0, 1, 2])
garagem = st.selectbox('Garagem', [0, 1, 2, 3])


imovel_simulado = np.array([zona, area, qualidade, ano, quali_aque, banheiros, comodos, lareiras, garagem]).reshape(1, -1)
preco_imovel_simulado = lr.predict(imovel_simulado)

if st.checkbox('Clique aqui para calcular o preço'):
    if resid.mean() > 0:
        st.markdown(f'Preço: {preco_imovel_simulado[0]:.2f}')
        st.markdown(f'Margem: Entre {(preco_imovel_simulado - resid).mean():.2f} e {(preco_imovel_simulado + resid).mean():.2f}')
    elif resid.mean() <= 0:
        st.markdown(f'Preço: {preco_imovel_simulado[0]:.2f}')
        st.markdown(f'Margem: Entre {(preco_imovel_simulado + resid).mean():.2f} e {(preco_imovel_simulado - resid).mean():.2f}')
