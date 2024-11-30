import streamlit as st

# Título e cabeçalhos
st.title("UniPisos")
st.header("Descomplicando os Dados de Memorial de Cálculo na Construção")
st.subheader("O que é Memorial de Cálculo?")
st.write("O memorial de cálculo é um documento que detalha todos os cálculos necessários para o projeto. Ele serve como um guia para a execução e a verificação das estruturas, garantindo que tudo esteja dentro das normas e regulamentos.")
st.subheader("Importância dos Dados")
st.write("Os dados contidos no memorial de cálculo são cruciais para a confiabilidade do projeto. Eles ajudam a evitar erros, economizar recursos e garantir a sustentabilidade das construções. Sem eles, o risco de falhas aumenta significativamente.")

st.image("https://images.tcdn.com.br/img/img_prod/614225/piso_ceramico_interno_polido_avolio_66x66cm_cx_2_18m_formigres_81143_2_b834d5c845372194ba34b12f1882dfb6.jpg", caption="Engenheiros", use_column_width=True)

def calcular_orcamento(area, preco_por_caixa, adicionar_sobra):
    """
    Calcula o orçamento total para o piso com base na área, preço por caixa e a opção de adicionar 20% de sobra.
    
    :param area: A área do piso em metros quadrados (m²)
    :param preco_por_caixa: O preço do piso por caixa (R$)
    :param adicionar_sobra: Booleano indicando se deve adicionar 20% de sobra
    :return: O orçamento total (R$)
    """
    area_por_caixa = 2.18  # Área coberta por cada caixa em m²
    if adicionar_sobra:
        area *= 1.20  # Adiciona 20% à área total
    caixas_necessarias = -(-area // area_por_caixa)  # Calcula o número de caixas necessárias, arredondando para cima
    orcamento_total = caixas_necessarias * preco_por_caixa
    return orcamento_total, caixas_necessarias

# Informações sobre o preço padrão
st.write("Para facilitar o cálculo, estamos considerando o preço padrão do piso de 66x66 cm como R$ 100,00 por caixa de 2,18 m².")

# Campos de entrada
area = st.number_input("Digite a área do piso em m²:", min_value=0.0, format="%.2f")
preco_por_caixa = 100.00  # Valor padrão
adicionar_sobra = st.checkbox("Deseja adicionar 20% de sobra?")

# Botão para calcular
if st.button("Calcular Orçamento"):
    orcamento, caixas_necessarias = calcular_orcamento(area, preco_por_caixa, adicionar_sobra)
    st.success(f"### O orçamento total para o piso é: R$ {orcamento:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias:.0f} caixas de piso.")

# Segunda opcao

st.subheader("Piso Cerâmico Retificado 66x66cm Caixa com 2,18 m² Extra Marmi Delux Mate Formigres")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000", caption="Engenheiros", use_column_width=True)
