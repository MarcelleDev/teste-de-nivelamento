import csv

def salvar_em_csv(dados, csv_path):
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if dados:
            writer.writerow(dados)
