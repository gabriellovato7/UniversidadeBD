CREATE TABLE IF NOT EXISTS Professor (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Departamento (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    chefe_id INT REFERENCES Professor(id)
);

CREATE TABLE IF NOT EXISTS Curso (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    coordenador_id INT REFERENCES Professor(id)
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
