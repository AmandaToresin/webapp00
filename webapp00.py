import streamlit as st

# Título e cabeçalhos
st.title("MABIL")
st.header("🔷 Calculadora de Pisos")
st.write("Bem-vindo ao nosso calculador de orçamento de piso! Aqui, você pode calcular de forma rápida e fácil quanto vai gastar para revestir sua área com pisos de sua escolha. Informe a metragem quadrada do ambiente, selecione o tipo de piso e obtenha uma estimativa precisa do custo total. Nosso objetivo é tornar o processo de planejamento da reforma mais simples e transparente, ajudando você a tomar decisões informadas e adequadas ao seu orçamento. Comece agora e descubra quanto seu projeto vai custar!")

# Adicionando CSS para estilizar o fundo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/ti/vetor-gratis/p1/7276935-padrao-icones-construcao-padrao-doodle-sem-costura-com-ferramentas-para-construcao-ilustracao-sobre-o-tema-da-construcao-vetor.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calcular_orcamento(area, preco_por_caixa, adicionar_sobra, area_por_caixa):
    if adicionar_sobra:
        area *= 1.20  # Adiciona 20% à área total
    caixas_necessarias = -(-area // area_por_caixa)  # Calcula o número de caixas necessárias, arredondando para cima
    orcamento_total = caixas_necessarias * preco_por_caixa
    return orcamento_total, caixas_necessarias

# Definindo os tipos de piso e suas características
pisos = {
    "Laminado": [
        {
            "nome": "Piso Laminado Eucafloor Prime Click Carvalho Canela",
            "preco_por_caixa": 119.90,
            "area_por_caixa": 2.36,
            "imagem": "https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg",
            "descricao": "Ideal para: sala de estar/jantar, quartos, corredores."
        }
    ],
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
        },
        {
            "nome": "Porcelanato Marmorizado Polido Borda Reta Interno 120x120cm",
            "preco_por_caixa": 541.18,
            "area_por_caixa": 2.48,
            "imagem": "https://acheiseupiso.com/cdn/shop/files/porcelanato_interno_polido_borda_reta_120x120cm_chloe_lux_90820170_b5ae_600x600_c41cdb0c-4520-49ff-8aad-13dd680c9493.jpg?v=1730828719",
            "descricao": "Ideal para: sala de estar/jantar, hall de entrada, cozinhas e banheiros, áreas comerciais de luxo."
        },
        {
            "nome": "Porcelanato Decorado Acetinado Borda Reta Externo 72x72cm",
            "preco_por_caixa": 121.50,
            "area_por_caixa": 2.59,
            "imagem": "https://d365e82sgxmduv.cloudfront.net/Custom/Content/Products/23/32/2332883_29549-porcelanato-cairo-externo-rust-72x72-cx2-59m-72111281-savane_z5_638300284526519484.webp",
            "descricao": "Ideal para: varandas e pátios, áreas de piscina, calçada e passarelas, jardins e áreas de convivência externas"
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
    ],
    "Retificado": [
        {
          "nome": "Piso Mont Blanc Satiny Retificado 101x101cm",
          "preco_por_caixa": 134.44,
          "area_por_caixa": 2.04,
          "imagem": "https://telhanorte.vtexassets.com/arquivos/ids/1272049-1200-auto",
          "descricao": "Ideal para: cozinhas, banheiros, áreas externas cobertas, hall de entrada e corredores."
        }
    ],
    "Granito": [
        {
          "nome": "Piso Interno Granito Casablanca Branco 57x57cm Extrata Stones",
          "preco_por_caixa": 394.71,
          "area_por_caixa": 0.975,
          "imagem": "https://cdn.leroymerlin.com.br/products/piso_ext_granito_casablanca_branco_57x57_m2_extratatones_91789663_91df_600x600.png",
          "descricao": "Ideal para: áreas internas de alto padrão, como salas de estar/jantar, cozinhas gourmet, banheiros luxuosos, escritórios e hall de entrada."
        }
    ]
}

# Contador global para gerar chaves únicas
contador = 0

def exibir_informacoes_piso(piso, categoria, idx):
    global contador
    contador += 1

    st.subheader(piso["nome"])
    st.image(piso["imagem"], caption=piso["descricao"], use_column_width=True)
    area = st.number_input(f"Digite a área do {piso['nome']} em m²:", min_value=0.0, format="%.2f", key=f'area_{contador}')
    adicionar_sobra = st.checkbox(f"Deseja adicionar 20% de sobra ao {piso['nome']}?", key=f'sobra_{contador}')
    if st.button(f"Calcular Orçamento para {piso['nome']}", key=f'btn_{contador}'):
        orcamento, caixas_necessarias = calcular_orcamento(area, piso["preco_por_caixa"], adicionar_sobra, piso["area_por_caixa"])
        st.success(f"O orçamento total para o {piso['nome']} é: R$ {orcamento:.2f}")
        st.info(f"Você precisará de aproximadamente {caixas_necessarias:.0f} caixas de {piso['nome']}.")

# Criando as abas para cada tipo de piso
abas = st.tabs(["Todos", "Laminado", "Cerâmico", "Vinílico", "Porcelanato", "Granito"])

# Adicionando conteúdo a cada aba
with abas[0]:
    st.header("Todos")
    for categoria, pisos_categoria in pisos.items():
        for idx, piso in enumerate(pisos_categoria):
            exibir_informacoes_piso(piso, categoria, idx)

with abas[1]:
    st.header("Laminado")
    for idx, piso in enumerate(pisos["Laminado"]):
        exibir_informacoes_piso(piso, "Laminado", idx)

with abas[2]:
    st.header("Cerâmico")
    for idx, piso in enumerate(pisos["Cerâmico"]):
        exibir_informacoes_piso(piso, "Cerâmico", idx)

with abas[3]:
    st.header("Vinílico")
    for idx, piso in enumerate(pisos["Vinílico"]):
        exibir_informacoes_piso(piso, "Vinílico", idx)

with abas[4]:
    st.header("Porcelanato")
    for idx, piso in enumerate(pisos["Porcelanato"]):
        exibir_informacoes_piso(piso, "Porcelanato", idx)

with abas[5]:
    st.header("Granito")
    for idx, piso in enumerate(pisos["Granito"]):
        exibir_informacoes_piso(piso, "Granito", idx)
