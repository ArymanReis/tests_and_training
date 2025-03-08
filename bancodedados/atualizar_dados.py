from conexao import conectar

def atualizar_dados(id, novo_salario):
  conn = conectar()
  if conn:
    try: 
      cursor = conn.cursor()
      cursor.execute("""
      UPDATE funcionarios SET salario = %s WHERE id = %s;
      """, (novo_salario, id))
      conn.commit()
      print("Dados atualizados com sucesso!")
    except Exception as e:
      print(f"Erro ao atualizar dados: {e}")
    finally:
      if conn:
        cursor.close()
        conn.close()
        print("Conexão encerrada.")

# Atualizando dados
if __name__ == "__main__":
  atualizar_dados(1, 5500.00)