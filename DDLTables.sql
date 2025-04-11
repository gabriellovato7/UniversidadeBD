CREATE TABLE IF NOT EXISTS Professor (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Departamento (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    chefe_id INT REFERENCES Professor(id),
    orcamento NUMERIC(12,2)
);

CREATE TABLE IF NOT EXISTS Curso (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    coordenador_id INT REFERENCES Professor(id),
    departamento_id INT NOT NULL REFERENCES Departamento(id)
);

CREATE TABLE IF NOT EXISTS Aluno (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL,
    curso_id INT REFERENCES Curso(id)
);

CREATE TABLE IF NOT EXISTS Disciplina (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS DisciplinaLecionada (
    id SERIAL PRIMARY KEY,
    professor_id INT REFERENCES Professor(id),
    disciplina_id INT REFERENCES Disciplina(id),
    semestre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS HistoricoEscolar (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES Aluno(id),
    disciplina_id INT REFERENCES Disciplina(id),
    semestre TEXT NOT NULL,
    nota NUMERIC(3,1),
    aprovado BOOLEAN
);

CREATE TABLE IF NOT EXISTS TCC (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    orientador_id INT REFERENCES Professor(id)
);

CREATE TABLE IF NOT EXISTS AlunoTCC (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES Aluno(id),
    tcc_id INT REFERENCES TCC(id)
);

CREATE TABLE IF NOT EXISTS MatrizCurricular (
    curso_id INT REFERENCES Curso(id),
    disciplina_id INT REFERENCES Disciplina(id),
    PRIMARY KEY (curso_id, disciplina_id)
);
