# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("UniPisos")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Descomplicando os Dados de Memorial de Cálculo na Construção")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("O que é Memorial de Cálculo?")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("O memorial de cálculo é um documento que detalha todos os cálculos necessários para o projeto. Ele serve como um guia para a execução e a verificação das estruturas, garantindo que tudo esteja dentro das normas e regulamentos.")

st.subheader("Importância dos Dados")

st.write("Os dados contidos no memorial de cálculo são cruciais para a confiabilidade do projeto. Eles ajudam a evitar erros, economizar recursos e garantir a sustentabilidade das construções. Sem eles, o risco de falhas aumenta significativamente.")

st.image("https://images.tcdn.com.br/img/img_prod/614225/piso_ceramico_interno_polido_avolio_66x66cm_cx_2_18m_formigres_81143_2_b834d5c845372194ba34b12f1882dfb6.jpg", caption="Engenheiros", use_column_width=True)

def calcular_orcamento(area, preco_por_m2, adicionar_sobra):
    """
    Calcula o orçamento total para o piso com base na área, preço por m² e a opção de adicionar 20% de sobra.
    
    :param area: A área do piso em metros quadrados (m²)
    :param preco_por_m2: O preço do piso por metro quadrado (R$)
    :param adicionar_sobra: Booleano indicando se deve adicionar 20% de sobra
    :return: O orçamento total (R$)
    """
    if adicionar_sobra:
        area *= 1.20  # Adiciona 20% à área total
    orcamento_total = area * preco_por_m2
    return orcamento_total

# Exemplo de uso
area = float(input("Digite a área do piso em m²: "))
preco_por_m2 = float(input("Digite o preço do piso por m² (R$): "))
adicionar_sobra = input("Deseja adicionar 20% de sobra? (sim/não): ").strip().lower() == "sim"

orcamento = calcular_orcamento(area, preco_por_m2, adicionar_sobra)
print(f"O orçamento total para o piso é: R$ {orcamento:.2f}")
