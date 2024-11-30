import streamlit as st

# Título e cabeçalhos
st.title("UniPisos")
st.header("Descomplicando os Dados de Memorial de Cálculo na Construção")
st.subheader("O que é Memorial de Cálculo?")
st.write("O memorial de cálculo é um documento que detalha todos os cálculos necessários para o projeto. Ele serve como um guia para a execução e a verificação das estruturas, garantindo que tudo esteja dentro das normas e regulamentos.")
st.subheader("Importância dos Dados")
st.write("Os dados contidos no memorial de cálculo são cruciais para a confiabilidade do projeto. Eles ajudam a evitar erros, economizar recursos e garantir a sustentabilidade das construções. Sem eles, o risco de falhas aumenta significativamente.")

st.image("https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg", caption="Engenheiros", use_column_width=True)

def calcular_orcamento(area, preco_por_caixa, adicionar_sobra, area_por_caixa):
    """
    Calcula o orçamento total para o piso com base na área, preço por caixa e a opção de adicionar 20% de sobra.
    
    :param area: A área do piso em metros quadrados (m²)
    :param preco_por_caixa: O preço do piso por caixa (R$)
    :param adicionar_sobra: Booleano indicando se deve adicionar 20% de sobra
    :param area_por_caixa: A área coberta por cada caixa em m²
    :return: O orçamento total (R$) e o número de caixas necessárias
    """
    if adicionar_sobra:
        area *= 1.20  # Adiciona 20% à área total
    caixas_necessarias = -(-area // area_por_caixa)  # Calcula o número de caixas necessárias, arredondando para cima
    orcamento_total = caixas_necessarias * preco_por_caixa
    return orcamento_total, caixas_necessarias

# Informações sobre os pisos
st.write("Estamos considerando dois tipos de piso:")
st.write("1. Piso Laminado de 66x66 cm (R$ 100,00 por caixa de 2,18 m²)")
st.write("2. Piso Cerâmico Retificado 66x66 cm (R$ 100,00 por caixa de 2,18 m²)")

# Campos de entrada
area = st.number_input("Digite a área do piso em m²:", min_value=0.0, format="%.2f")
adicionar_sobra = st.checkbox("Deseja adicionar 20% de sobra?")

# Botão para calcular o orçamento para o primeiro piso
