import pdfplumber

def extrair_dados_pdf(pdf_path):

    todas_paginas = []

    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()

            if tabela:
                todas_paginas.extend(tabela)

    return todas_paginas