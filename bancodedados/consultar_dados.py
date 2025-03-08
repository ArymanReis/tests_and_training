# consultar_dados.py
from conexao import conectar

def consultar_dados(id):
    """
    Consulta um funcionário na tabela 'funcionarios' pelo id.
    """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            # Comando SQL para buscar um funcionário pelo id
            cursor.execute("SELECT * FROM funcionarios WHERE id = %s;", (id,))
            resultado = cursor.fetchone()  # fetchone() retorna apenas um registro
            if resultado:
                print("Funcionário encontrado:")
                print(resultado)
            else:
                print(f"Nenhum funcionário encontrado com o id {id}.")
        except Exception as e:
            print(f"Erro ao consultar dados: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexão encerrada.")

# Exemplo de uso
if __name__ == "__main__":
    # Consulta o funcionário com id = 1
    consultar_dados(1)