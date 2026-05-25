from pydantic import BaseModel
from typing import Optional, List

# Entrada de dados de um estudante (repare no curso_id criando o relacionamento)
class EstudanteSchema(BaseModel):
    nome: str
    idade: int
    email: str
    curso_id: int

# Os campos de retorno de um estudante (consulta)
class EstudantePublicSchema(BaseModel):
    id: int
    nome: str
    idade: int
    email: str
    curso_id: int

# Campos opcionais para a edição do estudante
class EstudanteUpdateSchema(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    email: Optional[str] = None
    curso_id: Optional[int] = None

# Esquema de retorno de uma lista com todos os estudantes
class EstudanteListPublicSchema(BaseModel):
    estudantes: List[EstudantePublicSchema]