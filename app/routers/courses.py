from fastapi import APIRouter, status, HTTPException
from app.schemas.courses import CursoListPublicSchema, CursoPublicSchema, CursoSchema, CursoUpdateSchema
from typing import Optional, List

router = APIRouter()

# Simulando o banco de dados PRODUTOS que o professor usou, mas para CURSOS
CURSOS = []

@router.get(path='/', response_model=CursoListPublicSchema, status_code=status.HTTP_200_OK)
def curso_list():
    # Retorna a lista com todos os cursos cadastrados
    return {'cursos': CURSOS}


@router.post(path='/', response_model=CursoPublicSchema, status_code=status.HTTP_201_CREATED)
def curso_create(curso: CursoSchema):
    # A função model_dump() desestrutura o objeto para ser compreendido como um json
    curso_id = CursoPublicSchema(**curso.model_dump(), id=len(CURSOS)+1)
    CURSOS.append(curso_id)
    return curso_id


@router.put(path='/{id}', response_model=CursoPublicSchema, status_code=status.HTTP_201_CREATED)
def curso_update(id_curso: int, curso: CursoUpdateSchema):
    # Verifica se o id_curso está maior no intervalo de 1 ao tamanho da lista, caso contrário dispara uma exception.
    if id_curso > len(CURSOS) or id_curso < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course Not Found')
    
    curso_editado = CursoPublicSchema(**curso.model_dump(), id=id_curso)
    CURSOS[id_curso - 1] = curso_editado
    return curso_editado


@router.delete(path='/{id}')
def curso_delete(id_curso: int):
    # Mesma validação realizada no curso_update
    if id_curso > len(CURSOS) or id_curso < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course Not Found')
    
    # del deleta um determinado elemento da lista pelo seu índice
    del CURSOS[id_curso - 1]
    return {"detail": "Curso deletado com sucesso"}