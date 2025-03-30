import csv


def ajustar_abreviacoes(csv_path):

    with open(csv_path, mode='r', newline='', encoding='utf-8') as infile:
        leitor = csv.reader(infile)
        linhas = []

        for linha in leitor:

            linha = [col.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial") for col in linha]
            linhas.append(linha)


    with open(csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        escritor = csv.writer(outfile)
        escritor.writerows(linhas)


