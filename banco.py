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

    def inserir_departamento():
        nome = input("Digite o nome do departamento: ")
        chefe_id = input("Digite o ID do chefe (ou deixe em branco): ")

        if chefe_id:
            cursor.execute("SELECT id FROM Professor WHERE id = %s", (chefe_id,))
            if not cursor.fetchone():
                print(f"Erro: Não existe professor com ID {chefe_id}.")
                return
        else:
            chefe_id = None

        sql = "INSERT INTO Departamento (nome, chefe_id) VALUES (%s, %s)"
        cursor.execute(sql, (nome, chefe_id))
        conn.commit()
        print("Departamento inserido com sucesso!")

    def inserir_professor():
        nome = input("Digite o nome do professor: ")
        departamento_id = input("Digite o ID do departamento (ou deixe em branco): ")

        if departamento_id:
            cursor.execute("SELECT id FROM Departamento WHERE id = %s", (departamento_id,))
            if not cursor.fetchone():
                print(f"Erro: Departamento {departamento_id} não encontrado.")
                return
        else:
            departamento_id = None

        sql = "INSERT INTO Professor (nome, departamento_id) VALUES (%s, %s)"
        cursor.execute(sql, (nome, departamento_id))
        conn.commit()
        print("Professor inserido com sucesso!")

    def atualizar_departamento_professor():
        professor_id = input("Digite o ID do professor: ")
        novo_departamento_id = input("Digite o novo ID do departamento: ")

        cursor.execute("SELECT id FROM Departamento WHERE id = %s", (novo_departamento_id,))
        if not cursor.fetchone():
            print(f"Erro: Departamento Id {novo_departamento_id} não encontrado.")
            return

        cursor.execute("UPDATE Professor SET departamento_id = %s WHERE id = %s", (novo_departamento_id, professor_id))
        conn.commit()
        print("Departamento do professor atualizado com sucesso!")

    def atualizar_chefe_departamento():
        departamento_id = input("Digite o ID do departamento: ")
        novo_chefe_id = input("Digite o ID do novo chefe: ")

        cursor.execute("SELECT id FROM Professor WHERE id = %s", (novo_chefe_id,))
        if not cursor.fetchone():
            print(f"Erro: Professor Id {novo_chefe_id} não encontrado.")
            return

        cursor.execute("UPDATE Departamento SET chefe_id = %s WHERE id = %s", (novo_chefe_id, departamento_id))
        conn.commit()
        print("Chefe do departamento atualizado com sucesso!")

    while True:
        print("\n--- MENU ---")
        print("1 - Inserir Departamento")
        print("2 - Inserir Professor")
        print("3 - Atualizar Departamento do Professor")
        print("4 - Atualizar Chefe do Departamento")
        print("0 - Sair")

        opcao = input("Escolha a opção: ")

        if opcao == "1":
            inserir_departamento()
        elif opcao == "2":
            inserir_professor()
        elif opcao == "3":
            atualizar_departamento_professor()
        elif opcao == "4":
            atualizar_chefe_departamento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)
