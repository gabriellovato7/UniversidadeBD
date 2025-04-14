--1.
SELECT nome FROM Aluno;

--2.
SELECT id, nome FROM Professor;

--3.
SELECT nome, orcamento FROM Departamento WHERE orcamento > 50000;

--4.
SELECT DISTINCT a.nome
FROM Aluno a
JOIN HistoricoEscolar h ON a.id = h.aluno_id
JOIN Disciplina d ON h.disciplina_id = d.id
WHERE d.nome = 'Banco de Dados';

--5.
SELECT professor_id
FROM DisciplinaLecionada
GROUP BY professor_id
HAVING COUNT(DISTINCT disciplina_id) > 1;

--6.
SELECT a.id, a.nome
FROM Aluno a
JOIN AlunoTCC atcc ON a.id = atcc.aluno_id
JOIN TCC t ON atcc.tcc_id = t.id
WHERE t.orientador_id = 1;

--7.
SELECT a.nome
FROM Aluno a
JOIN Curso c ON a.curso_id = c.id
WHERE c.nome IN ('Ciência da Computação', 'Engenharia Elétrica');
