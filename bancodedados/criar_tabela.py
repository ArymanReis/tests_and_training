# criar_tabela.py
from conexao import conectar

def criar_tabela():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cargo VARCHAR(50),
                salario NUMERIC(10, 2)
            );
            """)
            conn.commit()
            print("Tabela 'funcionarios' criada!")
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexão encerrada.")

if __name__ == "__main__":
    criar_tabela()