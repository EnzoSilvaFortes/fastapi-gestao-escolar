from pydantic import BaseModel
from typing import Optional, List

# Entrada de dados de um curso
class CursoSchema(BaseModel):
    nome: str
    carga_horaria: int
    ativo: bool

# Os campos de retorno de um curso (consulta)
class CursoPublicSchema(BaseModel):
    id: int
    nome: str
    carga_horaria: int
    ativo: bool

# Campos opcionais para a edição do curso
class CursoUpdateSchema(BaseModel):
    nome: Optional[str] = None
    carga_horaria: Optional[int] = None
    ativo: Optional[bool] = None

# Esquema de retorno de uma lista com todos os cursos
class CursoListPublicSchema(BaseModel):
    cursos: List[CursoPublicSchema]