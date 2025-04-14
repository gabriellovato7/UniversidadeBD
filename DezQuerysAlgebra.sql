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

--8.
SELECT a.nome
FROM Aluno a
WHERE a.id NOT IN (
    SELECT DISTINCT he.aluno_id
    FROM HistoricoEscolar he
    JOIN Aluno al ON al.id = he.aluno_id
    JOIN Curso c ON al.curso_id = c.id
    JOIN Departamento d ON d.id = c.departamento_id
    WHERE d.nome ILIKE '%Engenharia%'
);

--9.
SELECT p.id, p.nome
FROM Professor p
JOIN DisciplinaLecionada dl ON p.id = dl.professor_id
JOIN HistoricoEscolar h ON h.disciplina_id = dl.disciplina_id AND h.semestre = dl.semestre
GROUP BY p.id, p.nome
HAVING COUNT(DISTINCT h.aluno_id) > 50;

--10.
SELECT h1.aluno_id, a.nome AS aluno_nome
FROM HistoricoEscolar h1
JOIN HistoricoEscolar h2 ON h1.aluno_id = h2.aluno_id
JOIN Aluno a ON h1.aluno_id = a.id
JOIN Disciplina d1 ON h1.disciplina_id = d1.id
JOIN Disciplina d2 ON h2.disciplina_id = d2.id
WHERE d1.nome = 'Engenharia de Software'
  AND d2.nome = 'Redes de Computadores'
  AND h1.semestre = h2.semestre
  AND h1.aprovado = TRUE
  AND h2.aprovado = TRUE;
