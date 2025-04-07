import psycopg2

host = "db.rcyhezijiupxtwfrycqv.supabase.co"
database = "postgres"
user = "postgres"
password = "12Banco34_8"
port = 5432

try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    cursor = conn.cursor()
    print("conexao realizada")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)
