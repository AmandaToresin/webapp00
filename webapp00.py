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
st.subheader("Piso Laminado Eucafloor Prime Click Carvalho Canela Cx 2,36m² (R$ 119,90 por caixa de 2,36 m²)")
st.image("https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg", caption="Ideal para: sala de estar/jantar, quartos, corredores.", use_column_width=True)
area1 = st.number_input("Digite a área do piso Laminado em m²:", min_value=0.0, format="%.2f")
adicionar_sobra1 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Laminado?", key='laminado')
if st.button("Calcular Orçamento para Piso Laminado"):
    orcamento1, caixas_necessarias1 = calcular_orcamento(area1, 119.90, adicionar_sobra1, 2.36)
    st.success(f"O orçamento total para o Piso Laminado é: R$ {orcamento1:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias1:.0f} caixas de Piso Laminado.")

# Segundo Piso - Piso Cerâmico
st.subheader("Piso Cerâmico Retificado 66x66 cm (R$ 89,90 por caixa de 2,18 m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000", caption="Ideal para: cozinhas, banheiro, áreas externas cobertas, sala de estar/ jantar, corredores e Halls.", use_column_width=True)
area2 = st.number_input("Digite a área do piso Cerâmico em m²:", min_value=0.0, format="%.2f")
adicionar_sobra2 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Cerâmico?", key='ceramico')
if st.button("Calcular Orçamento para Piso Cerâmico"):
    orcamento2, caixas_necessarias2 = calcular_orcamento(area2, 89.90, adicionar_sobra2, 2.18)
    st.success(f"O orçamento total para o Piso Cerâmico é: R$ {orcamento2:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias2:.0f} caixas de Piso Cerâmico.")

# Terceiro Piso - Piso Cerâmico 2
st.subheader("Piso Cerâmico Pedra Acetinado Borda Arredondada Externo 61,5x61,5cm (R$ 58,03 por caixa de 2,65m²)")
st.image("https://dcdn.mitiendanube.com/stores/002/797/263/products/piso-sao-tome-61x61-p1-a12fa27bc8dd7bbf5416763131496560-640-0.webp", caption="Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins.", use_column_width=True)
area3 = st.number_input("Digite a área do piso Cerâmico em m²:", min_value=0.0, format="%.2f")
adicionar_sobra3 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Cerâmico?", key='ceramico_pedra')
if st.button("Calcular Orçamento para Piso Cerâmico"):
    orcamento3, caixas_necessarias3 = calcular_orcamento(area3, 58.03, adicionar_sobra3, 2.65)
    st.success(f"O orçamento total para o Piso Cerâmico é: R$ {orcamento3:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias3:.0f} caixas de Piso Cerâmico.")

# Quarto Piso - Piso Vinílico
st.subheader("Piso Vinílico Vinil Forte Jacarandá 2x19x123cm (R$ 99,90 por caixa de 4,72m²)")
st.image("https://cdn.dooca.store/116921/products/jacaranda-hd-19x123-modelo-1_1600x1600+fill_ffffff.jpg?v=1692322213", caption="Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls.", use_column_width=True)
area4 = st.number_input("Digite a área do piso Vinílico em m²:", min_value=0.0, format="%.2f")
adicionar_sobra4 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Vinílico?", key='vinilico')
if st.button("Calcular Orçamento para Piso Vinílico"):
    orcamento4, caixas_necessarias4 = calcular_orcamento(area4, 99.90, adicionar_sobra4, 4.72)
    st.success(f"O orçamento total para o Piso Vinílico é: R$ {orcamento4:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias4:.0f} caixas de Piso Vinílico.")

# Quinto Piso - Piso Retificado
st.subheader("Piso Mont Blanc Satiny Retificado 101x101 cm (R$ 134,44 por caixa de 2,04 m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1272049-1200-auto", caption="Ideal para: cozinhas, banheiros, áreas externas cobertas, hall de entrada e corredores.", use_column_width=True)
area5 = st.number_input("Digite a área do piso Retificado em m²:", min_value=0.0, format="%.2f")
adicionar_sobra5 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Retificado?", key='retificado')
if st.button("Calcular Orçamento para Piso Retificado"):
    orcamento5, caixas_necessarias5 = calcular_orcamento(area5, 134.44, adicionar_sobra5, 2.04)
    st.success(f"O orçamento total para o Piso Retificado é: R$ {orcamento5:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias5:.0f} caixas de Piso Retificado.")

# Sexto Piso - Piso Porcelanato
st.subheader("Porcelanato Cimentício Acetinado Borda Arredondada Externo 60x60cm (R$ 152,12 por caixa de 1,8m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1272049-1200-auto", caption="Ideal para: áreas de piscina, garagens externas, calçadas e passarelas.", use_column_width=True)
area6 = st.number_input("Digite a área do piso Porcelanato em m²:", min_value=0.0, format="%.2f")
adicionar_sobra6 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Porcelanato?", key='porcelanato')
if st.button("Calcular Orçamento para Piso Porcelanato"):
    orcamento6, caixas_necessarias6 = calcular_orcamento(area6, 152.12, adicionar_sobra6, 1.8)
    st.success(f"O orçamento total para o Piso Porcelanato é: R$ {orcamento6:.2f
