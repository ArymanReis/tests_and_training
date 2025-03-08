# deletar_dados.py
from conexao import conectar

def deletar_dados(id):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            # Comando SQL para deletar um funcionário
            cursor.execute("""
            DELETE FROM funcionarios WHERE id = %s;
            """, (id,))
            conn.commit()
            print("Dados deletados com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar dados: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexão encerrada.")

# Exemplo de uso
if __name__ == "__main__":
    # Deleta o funcionário com id = 2
    deletar_dados(2)