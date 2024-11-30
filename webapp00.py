import streamlit as st

# Título e cabeçalhos
st.title("UniPisos")
st.header("Descomplicando os Dados de Memorial de Cálculo na Construção")
st.subheader("O que é Memorial de Cálculo?")
st.write("O memorial de cálculo é um documento que detalha todos os cálculos necessários para o projeto. Ele serve como um guia para a execução e a verificação das estruturas, garantindo que tudo esteja dentro das normas e regulamentos.")
st.subheader("Importância dos Dados")
st.write("Os dados contidos no memorial de cálculo são cruciais para a confiabilidade do projeto. Eles ajudam a evitar erros, economizar recursos e garantir a sustentabilidade das construções. Sem eles, o risco de falhas aumenta significativamente.")

st.image("https://images.tcdn.com.br/img/img_prod/614225/piso_ceramico_interno_polido_avolio_66x66cm_cx_2_18m_formigres_81143_2_b834d5c845372194ba34b12f1882dfb6.jpg", caption="Engenheiros", use_column_width=True)

def calcular_orcamento(area, preco_por_m2, adicionar_sobra):
    """
    Calcula o orçamento total para o piso com base na área, preço por m² e a opção de adicionar 20% de sobra.
    
    :param area: A área do piso em metros quadrados (m²)
    :param preco_por_m2: O preço do piso por metro quadrado (R$)
    :param adicionar_sobra: Booleano
