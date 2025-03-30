# Raciocínio Lógico para Estruturar Tabelas e Importar CSV
#Passo 1: Analisar o CSV -- Entender a estrutura do arquivo (colunas, tipos de dados, encoding).

#Passo 2: Criar a Tabela
#Mapear Colunas do CSV para Tipos SQL:
#registro_an
#cnpj
#razao_social
#data_registro
#Definir Chave Primária
#Criar um id artificial (auto-incremento) para garantir unicidade.

#Passo 3: Importar o CSV
#Garantir Compatibilidade de Encoding:
#Se o CSV tiver acentos, usar CHARACTER SET UTF8 ou LATIN1.
#Pular a primeira linha com IGNORE 1 ROWS.
#Mapear Colunas do CSV para a Tabela:
#A ordem das colunas na query deve refletir a ordem do CSV.
