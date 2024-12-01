import streamlit as st

# Título e cabeçalhos
st.title("MABIL")
st.image("https://pbs.twimg.com/media/GdveWw2XUAAO1Bf?format=png&name=small", width=200)
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
    "Laminado": [
        {
            "nome": "Piso Laminado Eucafloor Prime Click Carvalho Canela (Caixa com 2,36m² por R$219,90)",
            "preco_por_caixa": 219.90,
            "area_por_caixa": 2.36,
            "imagem": "https://static.estilohomecenter.com.br/public/estilohomecenter/imagens/produtos/piso-laminado-eucafloor-carvalho-canela-prime-click-cx-2-36m2-6651f11b0ba71.jpg",
            "descricao": "Ideal para: sala de estar/jantar, quartos, corredores."
        },
        {
            "nome": "Piso Laminado Click Elmo Ravena 136x21,7cm (Caixa com 2,36m² por R$58,40)",
            "preco_por_caixa": 58.40,
            "area_por_caixa": 2.36,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_laminado_click_elmo_ravena_136x21,7cm_m2_artens_89238114_bb19_600x600.jpg",
            "descricao": "Ideal para: sala de estar/jantar, quartos, corredores."
        },
        {
            "nome": "Piso Laminado Click Prime Nogueira Malaga 135,7x21,7cm (Caixa com 2,65m² por R$56.90)",
            "preco_por_caixa": 56.90,
            "area_por_caixa": 2.65,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_laminado_click_prime_click_malaga_7mmx2,35x13,8cm_m2_92252153_34b3_600x600.jpg",
            "descricao": "Ideal para: sala de estar/jantar, quartos, corredores."
        },
        {
            "nome": "Piso Laminado Click Twist Arenal 134x18,7cm (Caixa com 2,65m² por R$106,28)",
            "preco_por_caixa": 106.28,
            "area_por_caixa": 2.26,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_laminado_click_twist_twist_arenal_134x18,7cm_m2_durafloor_90847491_da74_600x600.jpg",
            "descricao": "Ideal para: sala de estar/jantar, quartos, corredores."
        }
    ],
    "Porcelanato": [
        {
            "nome": "Porcelanato Cimentício Acetinado Borda Arredondada Externo 60x60cm (Caixa com 1,80m² por R$152,12)",
            "preco_por_caixa": 152.12,
            "area_por_caixa": 1.80,
            "imagem": "https://cdagua.vtexassets.com/arquivos/ids/203687-800-800?v=638612236070930000&width=800&height=800&aspect=true",
            "descricao": "Ideal para: áreas de piscina, garagens externas, calçadas e passarelas."
        },
        {
            "nome": "Porcelanato Marmorizado Acetinado Borda Reta Interno 91x91cm (Caixa com 2,48m² por R$151,30)",
            "preco_por_caixa": 151.30,
            "area_por_caixa": 2.48,
            "imagem": "https://cdn.leroymerlin.com.br/products/porcelanato_acetinado_interno_91x91cm_blush_artens_92271886_6991_600x600.jpg",
            "descricao": "Ideal para: sala de estar/jantar, cozinhas e banheiros internos, escritórios e ambientes comerciais, corredores e Halls."
        },
        {
            "nome": "Porcelanato Marmorizado Polido Borda Reta Interno 120x120cm (Caixa com 2,48m² por R$541,18)",
            "preco_por_caixa": 541.18,
            "area_por_caixa": 2.48,
            "imagem": "https://acheiseupiso.com/cdn/shop/files/porcelanato_interno_polido_borda_reta_120x120cm_chloe_lux_90820170_b5ae_600x600_c41cdb0c-4520-49ff-8aad-13dd680c9493.jpg?v=1730828719",
            "descricao": "Ideal para: sala de estar/jantar, hall de entrada, cozinhas e banheiros, áreas comerciais de luxo."
        },
        {
            "nome": "Porcelanato Decorado Acetinado Borda Reta Externo 72x72cm (Caixa com 2,59m² por R$121,50)",
            "preco_por_caixa": 121.50,
            "area_por_caixa": 2.59,
            "imagem": "https://d365e82sgxmduv.cloudfront.net/Custom/Content/Products/23/32/2332883_29549-porcelanato-cairo-externo-rust-72x72-cx2-59m-72111281-savane_z5_638300284526519484.webp",
            "descricao": "Ideal para: varandas e pátios, áreas de piscina, calçada e passarelas, jardins e áreas de convivência externas"
        }
    ],
    "Cerâmico": [
        {
            "nome": "Piso Cerâmico Retificado 66x66 cm(Caixa com 2,18m² por R$89,90)",
            "preco_por_caixa": 89.90,
            "area_por_caixa": 2.18,
            "imagem": "https://telhanorte.vtexassets.com/arquivos/ids/1245914/7899436339296.jpg?v=638119047284200000",
            "descricao": "Ideal para: cozinhas, banheiro, áreas externas cobertas, sala de estar/jantar, corredores e Halls."
        },
        {
            "nome": "Piso Cerâmico Pedra Acetinado Borda Arredondada Externo 61,5x61,5cm (Caixa com 2,65m² por R$58.03)",
            "preco_por_caixa": 58.03,
            "area_por_caixa": 2.65,
            "imagem": "https://dcdn.mitiendanube.com/stores/002/797/263/products/piso-sao-tome-61x61-p1-a12fa27bc8dd7bbf5416763131496560-640-0.webp",
            "descricao": "Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins."
        },
        {
            "nome": "Piso Cerâmico Cimentício Borda Reta Externo 60,5x60,5cm Nevada (Caixa com 2,52m² por R$24,90)",
            "preco_por_caixa": 24.90,
            "area_por_caixa": 2.52,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_ceramico_cimenticio_acetinado_60,5x60,5_nevada_out_91801150_074d_600x600.jpg",
            "descricao": "Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins."
        },
        {
            "nome": "Piso Cerâmico Marmorizado Brilhante Borda Reta Interno 82x82 (Caixa com 2,69m² por R$31,87)",
            "preco_por_caixa": 31.87,
            "area_por_caixa": 2.69,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_ceramico_interno_brilhante_borda_reta_82x82cm_miragem_91900865_0002_600x600.jpg",
            "descricao": "Ideal para: indicado para área externas como varandas, garagens, calçadas, áreas de lazer e jardins."
        }
    ],
    "Vinílico": [
        {
            "nome": "Piso Vinílico Vinil Forte Jacarandá 2x19x123cm (Caixa com 4,72m² por R$120,24)",
            "preco_por_caixa": 120.90,
            "area_por_caixa": 4.72,
            "imagem": "https://cdn.dooca.store/116921/products/jacaranda-hd-19x123-modelo-1_1600x1600+fill_ffffff.jpg?v=1692322213",
            "descricao": "Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls."
        },
        {
            "nome": "Piso Vinílico Cola Injoy Papoula Madeira Bege(Caixa com 4,09m² por R$347,24)",
            "preco_por_caixa": 347.24,
            "area_por_caixa": 4.09,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_pvc_vini_injoy_papola_20,8x2x1,23_m2_tarkett_91068600_8007_600x600.jpg",
            "descricao": "Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls."
        },
        {
            "nome": "PISO VÍNILICO COLADO CARVALHO SUPREME 1,22M X 18CM(Caixa com 4,645m² por R$395,25)",
            "preco_por_caixa": 395.23,
            "area_por_caixa": 4.645,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_vinilico_colado_carvalho_supreme_1,22m_x_18cm_caixa_4,64_1571973568_7b0f_600x600.png",
            "descricao": "Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls."
        },
        {
            "nome": "Piso Laminado Click Affara Crema 25x135,7cm (Caixa com 2,71m² por R$49,90)",
            "preco_por_caixa": 49.90,
            "area_por_caixa": 2.71,
            "imagem": "https://cdn.leroymerlin.com.br/products/piso_laminado_click_adoro_affara_crema_25x135,7cm_m2_92158465_622e_600x600.jpg",
            "descricao": "Ideal para: áreas com baixa umidade como quartos, sala de estar/jantar, corredores e Halls."
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
abas = st.tabs(["Todos", "Laminado", "Cerâmico", "Vinílico", "Porcelanato"])

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
