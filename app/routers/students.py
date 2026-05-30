from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.students import EstudanteListPublicSchema, EstudantePublicSchema, EstudanteSchema, EstudanteUpdateSchema
from app.models.estudantes import Estudante
from app.core.database import get_session

router = APIRouter()

@router.get('/', response_model=EstudanteListPublicSchema, status_code=status.HTTP_200_OK)
def estudante_list(session: Session = Depends(get_session)):
    estudantes = session.scalars(select(Estudante)).all()
    return {'estudantes': list(estudantes)}

@router.post('/', response_model=EstudantePublicSchema, status_code=status.HTTP_201_CREATED)
def estudante_create(estudante: EstudanteSchema, session: Session = Depends(get_session)):
    novo_estudante = Estudante(**estudante.model_dump())
    session.add(novo_estudante)
    session.commit()
    session.refresh(novo_estudante)
    return novo_estudante

@router.put('/{id}', response_model=EstudantePublicSchema, status_code=status.HTTP_200_OK)
def estudante_update(id: int, estudante: EstudanteUpdateSchema, session: Session = Depends(get_session)):
    estudante_db = session.scalar(select(Estudante).where(Estudante.id == id))
    if not estudante_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student Not Found')
    
    for key, value in estudante.model_dump(exclude_unset=True).items():
        setattr(estudante_db, key, value)
        
    session.commit()
    session.refresh(estudante_db)
    return estudante_db

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def estudante_delete(id: int, session: Session = Depends(get_session)):
    estudante_db = session.scalar(select(Estudante).where(Estudante.id == id))
    if not estudante_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student Not Found')
    
    session.delete(estudante_db)
    session.commit()
    return {"detail": "Estudante deletado com sucesso"}