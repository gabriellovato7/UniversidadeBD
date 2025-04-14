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
