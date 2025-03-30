-- Criação do banco de dados (garantindo que não haja conflitos)
CREATE DATABASE IF NOT EXISTS and_dados; 
USE and_dados; 

-- Definição da tabela 'operadoras' com campos essenciais:
CREATE TABLE IF NOT EXISTS operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Chave primária autoincrementável (evita duplicatas)
    registro_an VARCHAR(20) NOT NULL,         -- Registro ANS
    cnpj VARCHAR(20) NOT NULL,                -- CNPJ
    razao_social VARCHAR(255) NOT NULL,       -- Razão social
    modalidade VARCHAR(100),                  -- Modalidade de operação (
    uf CHAR(2),                               -- Sigla do estado
    municipio VARCHAR(100),                   -- Município de atuação
    data_registro DATE                        -- Data de registro
);


-- Estudando
-- Tipos de Dados Adequados:
-- VARCHAR para textos variáveis.
-- CHAR(2) para siglas fixas (UF).
-- DATE para datas, facilitando filtros temporais.
-- Constraints de Integridade:
-- NOT NULL para campos obrigatórios.
-- AUTO_INCREMENT no id para evitar inserções manuais.
-- PRIMARY KEY	Identificador único e obrigatório de um registro. Só existe uma por tabela.

-- Preciso estudar mais Banco de Dados