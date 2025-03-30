import pandas as pd
from fastapi import APIRouter, Query

router = APIRouter()

# Carregar o CSV corretamente
df = pd.read_csv("dados/Relatorio_cadop.csv", delimiter=";", dtype=str)

# Ajustar nomes das colunas para garantir que estão corretos
colunas_principais = [
    "Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade",
    "Logradouro", "Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP",
    "DDD", "Telefone", "Fax", "Endereco_eletronico", "Representante",
    "Cargo_Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS"
]

df = df[colunas_principais]

# Normalizar os nomes para evitar erros de busca
df["Razao_Social"] = df["Razao_Social"].str.strip().str.lower()
df["Nome_Fantasia"] = df["Nome_Fantasia"].str.strip().str.lower()

@router.get("/buscar")
def buscar_operadoras(termo: str = Query(..., min_length=2, description="Termo de busca")):
    """Busca operadoras pelo Nome Fantasia ou Razão Social."""

    termo = termo.strip().lower()  # Remove espaços e padroniza

    resultado = df[
        df["Razao_Social"].str.contains(termo, case=False, na=False) |
        df["Nome_Fantasia"].str.contains(termo, case=False, na=False)
    ]

    if resultado.empty:
        return {"message": "Nenhuma operadora encontrada."}

    return resultado.to_dict(orient="records")
