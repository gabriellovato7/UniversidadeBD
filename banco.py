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
        orcamento = input("Digite o orçamento do departamento: ")
    
        if chefe_id:
            cursor.execute("SELECT id FROM Professor WHERE id = %s", (chefe_id,))
            if not cursor.fetchone():
                print(f"Erro: Não existe professor com ID {chefe_id}.")
                return
        else:
            chefe_id = None
    
        try:
            orcamento = float(orcamento)
        except ValueError:
            print("Erro: Orçamento deve ser um número.")
            return
    
        sql = "INSERT INTO Departamento (nome, chefe_id, orcamento) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, chefe_id, orcamento))
        conn.commit()
        print("Departamento inserido com sucesso!")


    def inserir_professor():
        nome = input("Digite o nome do professor: ")

        sql = "INSERT INTO Professor (nome) VALUES (%s)"
        cursor.execute(sql, (nome,))
        conn.commit()
        print("Professor inserido com sucesso!")

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
        departamento_id = input("Digite o ID do departamento (obrigatório): ")

        if not coordenador_id.strip():
            print("Não é possível inserir o curso sem um coordenador.")
            return

        if not departamento_id.strip():
            print("Não é possível inserir o curso sem um departamento.")
            return
    
        cursor.execute("SELECT id FROM Professor WHERE id = %s", (coordenador_id,))
        if not cursor.fetchone():
            print(f"Erro: Não existe professor com ID {coordenador_id}.")
            return

        cursor.execute("SELECT id FROM Departamento WHERE id = %s", (departamento_id,))
        if not cursor.fetchone():
            print(f"Erro: Não existe departamento com ID {departamento_id}.")
            return

        sql = "INSERT INTO Curso (nome, coordenador_id, departamento_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, coordenador_id, departamento_id))
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

        sql = "INSERT INTO Disciplina (nome, codigo) VALUES (%s, %s)"
        cursor.execute(sql, (nome, codigo))
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

    def inserir_matrizcurricular():
        curso_id = input("Digite o ID do curso: ")
        disciplina_id = input("Digite o ID da disciplina: ")

        cursor.execute("SELECT id FROM Curso WHERE id = %s", (curso_id,))
        if not cursor.fetchone():
            print(f"Erro: Curso com ID {curso_id} não encontrado.")
            return

        cursor.execute("SELECT id FROM Disciplina WHERE id = %s", (disciplina_id,))
        if not cursor.fetchone():
            print(f"Erro: Disciplina com ID {disciplina_id} não encontrada.")
            return

        sql = "INSERT INTO MatrizCurricular (curso_id, disciplina_id) VALUES (%s, %s)"
        cursor.execute(sql, (curso_id, disciplina_id))
        conn.commit()
        print("Disciplina e Curso adicionada a Matriz Curricular com sucesso!")

    def inserir_historico():
        aluno_id = input("Digite o ID do aluno: ")
        disciplina_id = input("Digite o ID da disciplina: ")
        semestre = input("Digite o semestre (ex: 5° semestre): ")
        nota = float(input("Digite a nota: "))
        aprovado_input = input("Aprovado? (1 para sim, 0 para não): ")

        aprovado = True if aprovado_input == "1" else False

        sql = "INSERT INTO HistoricoEscolar (aluno_id, disciplina_id, semestre, nota, aprovado) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (aluno_id, disciplina_id, semestre, nota, aprovado))
        conn.commit()
        print("Histórico inserido com sucesso!")

    def inserir_tcc():
        titulo = input("Digite o título do TCC: ")
        orientador_id = input("Digite o ID do orientador: ")
        sql = "INSERT INTO TCC (titulo, orientador_id) VALUES (%s, %s)"
        cursor.execute(sql, (titulo, orientador_id))
        conn.commit()
        print("TCC inserido com sucesso!")

    def inserir_aluno_tcc():
        aluno_id = input("Digite o ID do aluno: ")
        tcc_id = input("Digite o ID do TCC: ")
        sql = "INSERT INTO AlunoTCC (aluno_id, tcc_id) VALUES (%s, %s)"
        cursor.execute(sql, (aluno_id, tcc_id))
        conn.commit()
        print("Aluno vinculado ao TCC com sucesso!")

    while True:
        print("\n--- MENU ---")
        print("1 - Inserir Professor")
        print("2 - Inserir Departamento")
        print("3 - Atualizar Chefe do Departamento")
        print("4 - Inserir Curso")
        print("5 - Inserir Aluno")
        print("6 - Inserir Disciplina")
        print("7 - Inserir Disciplina Lecionada")
        print("8 - Inserir Matriz Curricular")
        print("9 - Inserir Histórico")
        print("10 - Inserir TCC")
        print("11 - Inserir Aluno TCC")
        print("0 - Sair")

        opcao = input("Escolha a opção: ")

        if opcao == "1":
            inserir_professor()
        elif opcao == "2":
            inserir_departamento()
        elif opcao == "3":
            atualizar_chefe_departamento()
        elif opcao == "4":
            inserir_curso()
        elif opcao == "5":
            inserir_aluno()
        elif opcao == "6":
            inserir_disciplina()
        elif opcao == "7":
            inserir_disciplina_lecionada()
        elif opcao == "8":
            inserir_matrizcurricular()
        elif opcao == "9":
            inserir_historico()
        elif opcao == "10":
            inserir_tcc()
        elif opcao == "11":
            inserir_aluno_tcc()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

    conn.close()
    print("conexao fechada")

except Exception as e:
    print("Erro de conexao: ", e)
