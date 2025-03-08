from conexao import conectar

def inserir_dados(nome, cargo, salario):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            # Corrigido o comando SQL (INSERT INTO) e os valores dinâmicos
            cursor.execute("""
            INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s);
            """, (nome, cargo, salario))
            conn.commit()
            print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexão encerrada.")

if __name__ == "__main__":
    # Inserindo dados
    inserir_dados("Abraão Reis", "Surfista", 15000)
    inserir_dados("Bruna Souza", "Nutricionista", 9000)
    inserir_dados("Jean Farias", "Logística", 4000)