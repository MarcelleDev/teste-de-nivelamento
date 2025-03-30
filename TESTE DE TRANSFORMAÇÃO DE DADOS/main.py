from extrair_tabela import extrair_dados_pdf
from salvar_csv import salvar_em_csv
from compactar_csv import compactar_csv
from ajuste_csv import ajustar_abreviacoes


pdf_path = "dados/Anexo_I.pdf"
csv_path = "dados/tabela_extraida.csv"
zip_path = "dados/Teste_Marcelle.zip"


dados_extraidos = extrair_dados_pdf(pdf_path)


if dados_extraidos:
    print("Dados extraídos com sucesso.")
else:
    print("Nenhum dado extraído do PDF.")


salvar_em_csv(dados_extraidos, csv_path)

print(f"Arquivo CSV salvo em {csv_path}")

ajustar_abreviacoes(csv_path)
print("Abreviações substituídas com sucesso!")

compactar_csv(csv_path, zip_path)

print(f"Arquivo ZIP salvo em {zip_path}")

