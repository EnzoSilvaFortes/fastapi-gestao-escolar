from fastapi import APIRouter, status, HTTPException
from app.schemas.students import EstudanteListPublicSchema, EstudantePublicSchema, EstudanteSchema, EstudanteUpdateSchema
from typing import Optional, List

router = APIRouter()

# Simulando o banco de dados PRODUTOS que o professor usou, mas para ESTUDANTES
ESTUDANTES = []

@router.get(path='/', response_model=EstudanteListPublicSchema, status_code=status.HTTP_200_OK)
def estudante_list():
    # Retorna a lista com todos os estudantes cadastrados
    return {'estudantes': ESTUDANTES}


@router.post(path='/', response_model=EstudantePublicSchema, status_code=status.HTTP_201_CREATED)
def estudante_create(estudante: EstudanteSchema):
    # A função model_dump() desestrutura o objeto para ser compreendido como um json
    estudante_id = EstudantePublicSchema(**estudante.model_dump(), id=len(ESTUDANTES)+1)
    ESTUDANTES.append(estudante_id)
    return estudante_id


@router.put(path='/{id}', response_model=EstudantePublicSchema, status_code=status.HTTP_201_CREATED)
def estudante_update(id_estudante: int, estudante: EstudanteUpdateSchema):
    # Verifica se o id_estudante está maior no intervalo de 1 ao tamanho da lista, caso contrário dispara uma exception.
    if id_estudante > len(ESTUDANTES) or id_estudante < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student Not Found')
    
    estudante_editado = EstudantePublicSchema(**estudante.model_dump(), id=id_estudante)
    ESTUDANTES[id_estudante - 1] = estudante_editado
    return estudante_editado


@router.delete(path='/{id}')
def estudante_delete(id_estudante: int):
    # Mesma validação realizada no estudante_update
    if id_estudante > len(ESTUDANTES) or id_estudante < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student Not Found')
    
    # del deleta um determinado elemento da lista pelo seu índice
    del ESTUDANTES[id_estudante - 1]
    return {"detail": "Estudante deletado com sucesso"}