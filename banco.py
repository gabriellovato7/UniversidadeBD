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

    def inserir_curso():
        nome = input("Digite o nome do curso: ")
        coordenador_id = input("Digite o ID do coordenador (obrigatório): ")

        if not coordenador_id.strip():
            print("Não é possível inserir o curso sem um coordenador.")
            return

        sql = "INSERT INTO Curso (nome, coordenador_id) VALUES (%s, %s)"
        cursor.execute(sql, (nome, coordenador_id))
        conn.commit()
        print("Curso inserido com sucesso!")


    def inserir_aluno():
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        curso_nome = input("Digite o Nome do curso do aluno: ")
    
        cursor.execute("SELECT id FROM Curso WHERE nome = %s", (curso_nome,))
        resultado = cursor.fetchone()

        if resultado:
            curso_id = resultado[0]
            sql = "INSERT INTO Aluno (nome, matricula, curso_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, matricula, curso_id))
            conn.commit()
            print("Aluno inserido com sucesso!")
        else:
            print(f"Curso '{curso_nome}' não encontrado. Verifique o nome e tente novamente.")
            
    def inserir_disciplina():
        nome = input("Digite o nome da disciplina: ")
        codigo = input("Digite o código da disciplina: ")
        curso_id = input("Digite o ID do curso da disciplina (obrigatório): ")

        if not curso_id.strip():
            print("Não é possível inserir a disciplina sem um curso.")
            return

        sql = "INSERT INTO Disciplina (nome, codigo, curso_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, codigo, curso_id))
        conn.commit()
        print("Disciplina inserida com sucesso!")

    def inserir_disciplina_lecionada():
        professor_id = input("Digite o ID do professor: ")
        disciplina_id = input("Digite o ID da disciplina: ")
        semestre = input("Digite o semestre: ")
        sql = "INSERT INTO DisciplinaLecionada (professor_id, disciplina_id, semestre) VALUES (%s, %s, %s)"
        cursor.execute(sql, (professor_id, disciplina_id, semestre))
        conn.commit()
        print("Disciplina lecionada inserida com sucesso!")

    while True:
        print("\n--- MENU ---")
        print("1 - Inserir Departamento")
        print("2 - Inserir Professor")
        print("3 - Atualizar Departamento do Professor")
        print("4 - Atualizar Chefe do Departamento")
        print("5 - Inserir Curso")
        print("6 - Inserir Aluno")
        print("7 - Inserir Disciplina")
        print("8 - Inserir Disciplina Lecionada")
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
        elif opcao == "5":
            inserir_curso()
        elif opcao == "6":
            inserir_aluno()
        elif opcao == "7":
            inserir_disciplina()
        elif opcao == "8":
            inserir_disciplina_lecionada()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)
