import streamlit as st

# Título e cabeçalhos
st.title("UniPisos")
st.header("Descomplicando os Dados de Memorial de Cálculo na Construção")
st.subheader("O que é Memorial de Cálculo?")
st.write("O memorial de cálculo é um documento que detalha todos os cálculos necessários para o projeto. Ele serve como um guia para a execução e a verificação das estruturas, garantindo que tudo esteja dentro das normas e regulamentos.")
st.subheader("Importância dos Dados")
st.write("Os dados contidos no memorial de cálculo são cruciais para a confiabilidade do projeto. Eles ajudam a evitar erros, economizar recursos e garantir a sustentabilidade das construções. Sem eles, o risco de falhas aumenta significativamente.")

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

# Primeiro Piso - Piso Laminado
st.subheader("Piso Laminado de 66x66 cm (R$ 100,00 por caixa de 2,18 m²)")
st.image("https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg", caption="Piso Laminado", use_column_width=True)
area1 = st.number_input("Digite a área do piso Laminado em m²:", min_value=0.0, format="%.2f")
adicionar_sobra1 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Laminado?", key='laminado')
if st.button("Calcular Orçamento para Piso Laminado"):
    orcamento1, caixas_necessarias1 = calcular_orcamento(area1, 100.00, adicionar_sobra1, 2.18)
    st.success(f"### O orçamento total para o Piso Laminado é: R$ {orcamento1:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias1:.0f} caixas de Piso Laminado.")

# Segundo Piso - Piso Cerâmico
st.subheader("Piso Cerâmico Retificado 66x66 cm (R$ 100,00 por caixa de 2,18 m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000", caption="Piso Cerâmico", use_column_width=True)
area2 = st.number_input("Digite a área do piso Cerâmico em m²:", min_value=0.0, format="%.2f")
adicionar_sobra2 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Cerâmico?", key='ceramico')
if st.button("Calcular Orçamento para Piso Cerâmico"):
    orcamento2, caixas_necessarias2 = calcular_orcamento(area2, 100.00, adicionar_sobra2, 2.18)
    st.success(f"### O orçamento total para o Piso Cerâmico é: R$ {orcamento2:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias2:.0f} caixas de Piso Cerâmico.")
