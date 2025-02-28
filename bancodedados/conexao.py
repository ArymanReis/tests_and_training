# conexao.py
import psycopg2

def conectar():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="empresa",
            user="postgres",
            password="aluno123"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

if __name__ == "__main__":
    conn = conectar()
    if conn:
        print("Conexão bem-sucedida!")
        conn.close()
    else:
        print("Falha na conexão.")