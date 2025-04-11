1.
SELECT 
    a.nome AS aluno,
    d.codigo AS cod_disciplina,
    d.nome AS disciplina,
    h.semestre,
    h.nota,
    h.aprovado
FROM 
    HistoricoEscolar h
JOIN 
    Aluno a ON a.id = h.aluno_id
JOIN 
    Disciplina d ON d.id = h.disciplina_id
WHERE 
    h.aluno_id IN (
        SELECT 
            h1.aluno_id
        FROM 
            HistoricoEscolar h1
        WHERE 
            h1.aprovado = FALSE
        INTERSECT
        SELECT 
            h2.aluno_id
        FROM 
            HistoricoEscolar h2
        WHERE 
            h2.aprovado = TRUE
    )
ORDER BY 
    h.aluno_id,
    d.id,
    h.semestre;


3.
SELECT 
    c.nome AS curso,
    d.nome AS disciplina,
    d.codigo
FROM 
    MatrizCurricular m
JOIN 
    Curso c ON c.id = m.curso_id
JOIN 
    Disciplina d ON d.id = m.disciplina_id
WHERE 
    c.nome = 'Ciências de Dados';

SELECT 
    c.nome AS curso,
    d.nome AS disciplina,
    d.codigo
FROM 
    MatrizCurricular m
JOIN 
    Curso c ON c.id = m.curso_id
JOIN 
    Disciplina d ON d.id = m.disciplina_id
WHERE 
    c.nome = 'Ciências da Computação';
