import psycopg2

# Parâmetros de conexão com o banco de dados
hostname = "dpg-cnjjegev3ddc738d6r70-a"
port = "5432"
database = "banco_evento_empresa"
username = "banco_evento_empresa_user"
password = "X7rECD5KwCQeMWsoyvl0awoE2SlSorvd"

# Conectando ao banco de dados
try:
    connection = psycopg2.connect(
        dbname=database,
        user=username,
        password=password,
        host=hostname,
        port=port
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()

# Exemplo de consulta
cursor = connection.cursor()
query = "SELECT * FROM sua_tabela;"
cursor.execute(query)

# Obtendo os resultados da consulta
rows = cursor.fetchall()

# Exibindo os resultados
for row in rows:
    print(row)

# Fechando a conexão com o banco de dados
connection.close()
