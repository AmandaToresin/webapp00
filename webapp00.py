import streamlit as st

# Título e cabeçalhos
st.title("MABIL")
st.header("🔷 Calculadora de Pisos")
st.write("Bem-vindo ao nosso calculador de orçamento de piso! Aqui, você pode calcular de forma rápida e fácil quanto vai gastar para revestir sua área com pisos de sua escolha. Informe a metragem quadrada do ambiente, selecione o tipo de piso e obtenha uma estimativa precisa do custo total. Nosso objetivo é tornar o processo de planejamento da reforma mais simples e transparente, ajudando você a tomar decisões informadas e adequadas ao seu orçamento. Comece agora e descubra quanto seu projeto vai custar!")

def calcular_orcamento(area, preco_por_caixa, adicionar_sobra, area_por_caixa):
    if adicionar_sobra:
        area *= 1.20  # Adiciona 20% à área total
    caixas_necessarias = -(-area // area_por_caixa)  # Calcula o número de caixas necessárias, arredondando para cima
    orcamento_total = caixas_necessarias * preco_por_caixa
    return orcamento_total, caixas_necessarias


# Definindo os tipos de piso e suas características
pisos = {
    "Porcelanato": [
        {
            "nome": "Porcelanato Cimentício Acetinado Borda Arredondada Externo 60x60cm",
            "preco_por_caixa": 152.12,
            "area_por_caixa": 1.8,
            "imagem": "https://cdagua.vtexassets.com/arquivos/ids/203687-800-800?v=638612236070930000&width=800&height=800&aspect=true",
            "descricao": "Ideal para: áreas de piscina, garagens externas, calçadas e passarelas."
        },
        {
            "nome": "Porcelanato Marmorizado Acetinado Borda Reta Interno 91x91cm",
            "preco_por_caixa": 151.30,
            "area_por_caixa": 2.48,
            "imagem": "https://cdn.leroymerlin.com.br/products/porcelanato_acetinado_interno_91x91cm_blush_artens_92271886_6991_600x600.jpg",
            "descricao": "Ideal para: sala de estar/jantar, cozinhas e banheiros internos, escritórios e ambientes comerciais, corredores e Halls."
        }
    ],
    "Cerâmico": [
        {
            "nome": "Piso Cerâmico Retificado 66x66 cm",
            "preco_por_caixa": 89.90,
            "area_por_caixa": 2.18,
            "imagem": "https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000",
            "descricao": "Ideal para: cozinhas, banheiro, áreas externas cobertas, sala de estar/jantar, corredores e Halls."
        },
        {
            "nome": "Piso Cerâmico Pedra Acetinado Borda Arredondada Externo 61,5x61,5cm",
            "preco_por_caixa": 58.03,
            "area_por_caixa": 2.65,
            "imagem": "https://dcdn.mitiendanube.com/stores/002/797/263/products/piso-sao-tome-61x61-p1-a12fa27bc8dd7bbf5416763131496560-640-0.webp",
            "descricao": "Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins."
        }
    ],
    "Vinílico": [
        {
            "nome": "Piso Vinílico Vinil Forte Jacarandá 2x19x123cm",
            "preco_por_caixa": 99.90,
            "area_por_caixa": 4.72,
            "imagem": "https://cdn.dooca.store/116921/products/jacaranda-hd-19x123-modelo-1_1600x1600+fill_ffffff.jpg?v=1692322213",
            "descricao": "Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls."
        }
    ]
}

# Adicionando o filtro para selecionar a categoria de piso
categoria_piso = st.selectbox("Selecione a categoria de piso", ["Porcelanato", "Cerâmico", "Vinílico"])

# Encontrando o piso selecionado
piso_selecionado = next(piso for piso in pisos[categoria_piso] if piso["nome"] == tipo_piso)

# Exibindo informações do piso selecionado
st.subheader(piso_selecionado["nome"])
st.image(piso_selecionado["imagem"], caption=piso_selecionado["descricao"], use_column_width=True)
area = st.number_input(f"Digite a área do {categoria_piso} em m²:", min_value=0.0, format="%.2f", key='area')
adicionar_sobra = st.checkbox(f"Deseja adicionar 20% de sobra ao {categoria_piso}?", key='sobra')
if st.button(f"Calcular Orçamento para {categoria_piso}", key='btn'):
    orcamento, caixas_necessarias = calcular_orcamento(area, piso_selecionado["preco_por_caixa"], adicionar_sobra, piso_selecionado["area_por_caixa"])
    st.success(f"O orçamento total para o {categoria_piso} é: R$ {orcamento:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias:.0f} caixas de {categoria_piso}.")


# Primeiro Piso - Piso Laminado
st.subheader("Piso Laminado Eucafloor Prime Click Carvalho Canela Cx 2,36m² (R$ 119,90 por caixa de 2,36 m²)")
st.image("https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg", caption="Ideal para: sala de estar/jantar, quartos, corredores.", use_column_width=True)
area1 = st.number_input("Digite a área do piso Laminado em m²:", min_value=0.0, format="%.2f", key='area1')
adicionar_sobra1 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Laminado?", key='laminado')
if st.button("Calcular Orçamento para Piso Laminado", key='btn_laminado'):
    orcamento1, caixas_necessarias1 = calcular_orcamento(area1, 119.90, adicionar_sobra1, 2.36)
    st.success(f"O orçamento total para o Piso Laminado é: R$ {orcamento1:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias1:.0f} caixas de Piso Laminado.")

# Segundo Piso - Piso Cerâmico
st.subheader("Piso Cerâmico Retificado 66x66 cm (R$ 89,90 por caixa de 2,18 m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000", caption="Ideal para: cozinhas, banheiro, áreas externas cobertas, sala de estar/ jantar, corredores e Halls.", use_column_width=True)
area2 = st.number_input("Digite a área do piso Cerâmico em m²:", min_value=0.0, format="%.2f", key='area2')
adicionar_sobra2 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Cerâmico?", key='ceramico')
if st.button("Calcular Orçamento para Piso Cerâmico", key='btn_ceramico'):
    orcamento2, caixas_necessarias2 = calcular_orcamento(area2, 89.90, adicionar_sobra2, 2.18)
    st.success(f"O orçamento total para o Piso Cerâmico é: R$ {orcamento2:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias2:.0f} caixas de Piso Cerâmico.")

# Terceiro Piso - Piso Cerâmico 2
st.subheader("Piso Cerâmico Pedra Acetinado Borda Arredondada Externo 61,5x61,5cm (R$ 58,03 por caixa de 2,65m²)")
st.image("https://dcdn.mitiendanube.com/stores/002/797/263/products/piso-sao-tome-61x61-p1-a12fa27bc8dd7bbf5416763131496560-640-0.webp", caption="Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins.", use_column_width=True)
area3 = st.number_input("Digite a área do piso Cerâmico em m²:", min_value=0.0, format="%.2f", key='area3')
adicionar_sobra3 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Cerâmico?", key='ceramico_pedra')
if st.button("Calcular Orçamento para Piso Cerâmico", key='btn_ceramico2'):
    orcamento3, caixas_necessarias3 = calcular_orcamento(area3, 58.03, adicionar_sobra3, 2.65)
    st.success(f"O orçamento total para o Piso Cerâmico é: R$ {orcamento3:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias3:.0f} caixas de Piso Cerâmico.")

# Quarto Piso - Piso Vinílico
st.subheader("Piso Vinílico Vinil Forte Jacarandá 2x19x123cm (R$ 99,90 por caixa de 4,72m²)")
st.image("https://cdn.dooca.store/116921/products/jacaranda-hd-19x123-modelo-1_1600x1600+fill_ffffff.jpg?v=1692322213", caption="Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls.", use_column_width=True)
area4 = st.number_input("Digite a área do piso Vinílico em m²:", min_value=0.0, format="%.2f", key='area4')
adicionar_sobra4 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Vinílico?", key='vinilico')
if st.button("Calcular Orçamento para Piso Vinílico", key='btn_vinilico'):
    orcamento4, caixas_necessarias4 = calcular_orcamento(area4, 99.90, adicionar_sobra4, 4.72)
    st.success(f"O orçamento total para o Piso Vinílico é: R$ {orcamento4:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias4:.0f} caixas de Piso Vinílico.")

# Quinto Piso - Piso Retificado
st.subheader("Piso Mont Blanc Satiny Retificado 101x101 cm (R$ 134,44 por caixa de 2,04 m²)")
st.image("https://telhanorte.vtexassets.com/arquivos/ids/1272049-1200-auto", caption="Ideal para: cozinhas, banheiros, áreas externas cobertas, hall de entrada e corredores.", use_column_width=True)
area5 = st.number_input("Digite a área do piso Retificado em m²:", min_value=0.0, format="%.2f", key='area5')
adicionar_sobra5 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Retificado?", key='retificado')
if st.button("Calcular Orçamento para Piso Retificado", key='btn_retificado'):
    orcamento5, caixas_necessarias5 = calcular_orcamento(area5, 134.44, adicionar_sobra5, 2.04)
    st.success(f"O orçamento total para o Piso Retificado é: R$ {orcamento5:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias5:.0f} caixas de Piso Retificado.")

# Sexto Piso - Piso Porcelanato
st.subheader("Porcelanato Cimentício Acetinado Borda Arredondada Externo 60x60cm (R$ 152,12 por caixa de 1,8m²)")
st.image("https://cdagua.vtexassets.com/arquivos/ids/203687-800-800?v=638612236070930000&width=800&height=800&aspect=true", caption="Ideal para: áreas de piscina, garagens externas, calçadas e passarelas.", use_column_width=True)
area6 = st.number_input("Digite a área do piso Porcelanato em m²:", min_value=0.0, format="%.2f", key='area6')
adicionar_sobra6 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Porcelanato?", key='porcelanato')
if st.button("Calcular Orçamento para Piso Porcelanato", key='btn_porcelanato'):
    orcamento6, caixas_necessarias6 = calcular_orcamento(area6, 152.12, adicionar_sobra6, 1.8)
    st.success(f"O orçamento total para o Piso Porcelanato é: R$ {orcamento6:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias6:.0f} caixas de Piso Porcelanato.")

# Sétimo Piso - Porcelanato Marmorizado
st.subheader("Porcelanato Marmorizado Acetinado Borda Reta Interno 91x91cm (R$ 151,30 por caixa de 2,48m²)")
st.image("https://cdn.leroymerlin.com.br/products/porcelanato_acetinado_interno_91x91cm_blush_artens_92271886_6991_600x600.jpg", caption="Ideal para: sala de estar/jantar, cozinhas e banheiros internos, escritórios e ambientes comerciais, corredores e Halls.", use_column_width=True)
area7 = st.number_input("Digite a área do Porcelanato Marmorizado em m²:", min_value=0.0, format="%.2f", key='area7')
adicionar_sobra7 = st.checkbox("Deseja adicionar 20% de sobra ao Porcelanato Marmorizado?", key='marmorizado')
if st.button("Calcular Orçamento para Porcelanato Marmorizado", key='btn_marmorizado'):
    orcamento7, caixas_necessarias7 = calcular_orcamento(area7, 151.30, adicionar_sobra7, 2.48)
    st.success(f"O orçamento total para o Porcelanato Marmorizado é: R$ {orcamento7:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias7:.0f} caixas de Porcelanato Marmorizado.")

# Oitavo Piso - Porcelanato Marmorizado Polido
st.subheader("Porcelanato Marmorizado Polido Borda Reta Interno 120x120cm (R$ 541,18 por caixa de 2,88m²)")
st.image("https://acheiseupiso.com/cdn/shop/files/porcelanato_interno_polido_borda_reta_120x120cm_chloe_lux_90820170_b5ae_600x600_c41cdb0c-4520-49ff-8aad-13dd680c9493.jpg?v=1730828719", caption="Ideal para: sala de estar/jantar, hall de entrada, cozinhas e banheiros, áreas comerciais de luxo.", use_column_width=True)
area8 = st.number_input("Digite a área do Porcelanato Marmorizado Polido em m²:", min_value=0.0, format="%.2f", key='area8')
adicionar_sobra8 = st.checkbox("Deseja adicionar 20% de sobra ao Porcelanato Marmorizado Polido?", key='marmorizado_polido')
if st.button("Calcular Orçamento para Porcelanato Marmorizado Polido", key='btn_marmorizado_polido'):
    orcamento8, caixas_necessarias8 = calcular_orcamento(area8, 541.18, adicionar_sobra8, 2.88)
    st.success(f"O orçamento total para o Porcelanato Marmorizado Polido é: R$ {orcamento8:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias8:.0f} caixas de Porcelanato Marmorizado Polido.")

# Nono Piso - Porcelanato Decorado
st.subheader("Porcelanato Decorado Acetinado Borda Reta Externo 72x72cm (R$ 121,50 por caixa de 2,59m²)")
st.image("https://d365e82sgxmduv.cloudfront.net/Custom/Content/Products/23/32/2332883_29549-porcelanato-cairo-externo-rust-72x72-cx2-59m-72111281-savane_z5_638300284526519484.webp", caption="Ideal para: varandas e pátios, áreas de piscina, calçada e passarelas, jardins e áreas de convivência externas", use_column_width=True)
area9 = st.number_input("Digite a área do Porcelanato Decorado em m²:", min_value=0.0, format="%.2f", key='area9')
adicionar_sobra9 = st.checkbox("Deseja adicionar 20% de sobra ao Porcelanato Decorado?", key='decorado')
if st.button("Calcular Orçamento para Porcelanato Decorado", key='btn_decorado'):
    orcamento9, caixas_necessarias9 = calcular_orcamento(area9, 121.50, adicionar_sobra9, 2.59)
    st.success(f"O orçamento total para o Porcelanato Decorado é: R$ {orcamento9:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias9:.0f} caixas de Porcelanato Decorado.")

# Décimo Piso - Piso Interno Granito Casablanca
st.subheader("Piso Interno Granito Casablanca Branco 57x57cm Extrata Stones (R$ 394,71 por caixa de 0,975m²)")
st.image("https://cdn.leroymerlin.com.br/products/piso_ext_granito_casablanca_branco_57x57_m2_extratatones_91789663_91df_600x600.png", caption="Ideal para: áreas internas de alto padrão, como salas de estar/jantar, cozinhas gourmet, banheiros luxuosos, escritórios e hall de entrada.", use_column_width=True)
area10 = st.number_input("Digite a área do Piso Interno Granito Casablanca em m²:", min_value=0.0, format="%.2f", key='area10')
adicionar_sobra10 = st.checkbox("Deseja adicionar 20% de sobra ao Piso Interno Granito Casablanca?", key='granito_casablanca')
if st.button("Calcular Orçamento para Piso Interno Granito Casablanca", key='btn_granito_casablanca'):
    orcamento10, caixas_necessarias10 = calcular_orcamento(area10, 394.71, adicionar_sobra10, 0.975)
    st.success(f"O orçamento total para o Piso Interno Granito Casablanca é: R$ {orcamento10:.2f}")
    st.info(f"Você precisará de aproximadamente {caixas_necessarias10:.0f} caixas de Piso Interno Granito Casablanca.")

