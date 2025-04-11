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


2.
    SELECT 
    p.nome AS professor,
    t.titulo AS tcc,
    a.nome AS aluno
FROM 
    TCC t
JOIN 
    Professor p ON p.id = t.orientador_id
JOIN 
    AlunoTCC at ON at.tcc_id = t.id
JOIN 
    Aluno a ON a.id = at.aluno_id
WHERE 
    p.id = 1  
ORDER BY 
    t.titulo;


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


4.
SELECT 
    d.codigo,
    d.nome AS disciplina,
    p.nome AS professor
FROM 
    HistoricoEscolar h
JOIN 
    Disciplina d ON d.id = h.disciplina_id
JOIN 
    DisciplinaLecionada dl ON dl.disciplina_id = d.id AND dl.semestre = h.semestre
JOIN 
    Professor p ON p.id = dl.professor_id
WHERE 
    h.aluno_id = 1 
ORDER BY 
    h.semestre;


5.
SELECT 
    p.nome AS professor,
    COALESCE(d.nome, 'nenhum') AS departamento_chefiado,
    COALESCE(c.nome, 'nenhum') AS curso_coordenado
FROM 
    Professor p
LEFT JOIN 
    Departamento d ON d.chefe_id = p.id
LEFT JOIN 
    Curso c ON c.coordenador_id = p.id
ORDER BY 
    p.nome;
