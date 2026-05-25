# API de Gestão Escolar

Este projeto consiste na **1ª Entrega** da atividade avaliativa da disciplina de Desenvolvimento de APIs com FastAPI. A aplicação foi estruturada seguindo rigorosamente os padrões arquiteturais exigidos, segregando rotas (`routers/`), esquemas de validação (`schemas/`) e centralizando a aplicação no arquivo `main.py`.

## Cenário Escolhido e Entidades

O nicho de mercado escolhido para este projeto foi o **Educacional**, focando no gerenciamento e relacionamento entre cursos e estudantes.

### 1. Entidade: Curso (Course)
Representa os cursos ofertados pela instituição.
* `id`: Inteiro (Identificador único gerado automaticamente)
* `nome`: String (Nome do curso)
* `carga_horaria`: Inteiro (Duração do curso em horas)
* `ativo`: Booleano (Status se o curso está ativo ou não)

### 2. Entidade: Estudante (Student)
Representa os alunos matriculados na instituição e possui relacionamento com a entidade Curso.
* `id`: Inteiro (Identificador único gerado automaticamente)
* `nome`: String (Nome completo do estudante)
* `idade`: Inteiro (Idade do aluno)
* `email`: String (Correio eletrônico do aluno)
* `curso_id`: Inteiro (Chave de relacionamento que vincula o estudante ao seu respectivo curso)

