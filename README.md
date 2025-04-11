# UniversidadeBD

## Diagrama Modelo Entidade Relacionamento (MER)

```mermaid
erDiagram
    PROFESSOR ||--o| DEPARTAMENTO : chefia
    PROFESSOR ||--o| CURSO : coordena
    PROFESSOR ||--|{ DISCIPLINALECIONADA : leciona
    PROFESSOR ||--o{ TCC : orienta

    CURSO ||--o{ ALUNO : possui
    CURSO ||--o{ MATRIZCURRICULAR : contem
    CURSO ||--o{ DISCIPLINA : possui
    CURSO ||--o| DEPARTAMENTO : pertence

    DISCIPLINA ||--o{ DISCIPLINALECIONADA : pertence
    DISCIPLINA ||--o{ HISTORICOESCOLAR : aparece
    DISCIPLINA ||--o{ MATRIZCURRICULAR : incluida

    ALUNO ||--o{ HISTORICOESCOLAR : possui
    ALUNO ||--o{ ALUNOTCC : participa
    TCC ||--o{ ALUNOTCC : tem_aluno

    PROFESSOR {
        int id
        text nome
    }

    DEPARTAMENTO {
        int id
        text nome
        int chefe_id
        numeric orcamento
    }

    CURSO {
        int id
        text nome
        int coordenador_id
        int departamento_id
    }

    ALUNO {
        int id
        text nome
        text matricula
        int curso_id
    }

    DISCIPLINA {
        int id
        text nome
        text codigo
    }

    DISCIPLINALECIONADA {
        int id
        int professor_id
        int disciplina_id
        text semestre
    }

    HISTORICOESCOLAR {
        int id
        int aluno_id
        int disciplina_id
        text semestre
        numeric nota
        boolean aprovado
    }

    TCC {
        int id
        text titulo
        int orientador_id
    }

    ALUNOTCC {
        int id
        int aluno_id
        int tcc_id
    }

    MATRIZCURRICULAR {
        int curso_id
        int disciplina_id
    }