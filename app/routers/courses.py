from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.courses import CursoListPublicSchema, CursoPublicSchema, CursoSchema, CursoUpdateSchema
from app.models.cursos import Curso
from app.core.database import get_session

router = APIRouter()

@router.get('/', response_model=CursoListPublicSchema, status_code=status.HTTP_200_OK)
def curso_list(session: Session = Depends(get_session)):
    cursos = session.scalars(select(Curso)).all()
    return {'cursos': list(cursos)}

@router.post('/', response_model=CursoPublicSchema, status_code=status.HTTP_201_CREATED)
def curso_create(curso: CursoSchema, session: Session = Depends(get_session)):
    novo_curso = Curso(**curso.model_dump())
    session.add(novo_curso)
    session.commit()
    session.refresh(novo_curso)
    return novo_curso

@router.put('/{id}', response_model=CursoPublicSchema, status_code=status.HTTP_200_OK)
def curso_update(id: int, curso: CursoUpdateSchema, session: Session = Depends(get_session)):
    curso_db = session.scalar(select(Curso).where(Curso.id == id))
    if not curso_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course Not Found')
    
    for key, value in curso.model_dump(exclude_unset=True).items():
        setattr(curso_db, key, value)
        
    session.commit()
    session.refresh(curso_db)
    return curso_db

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def curso_delete(id: int, session: Session = Depends(get_session)):
    curso_db = session.scalar(select(Curso).where(Curso.id == id))
    if not curso_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Course Not Found')
    
    session.delete(curso_db)
    session.commit()
    return {"detail": "Curso deletado com sucesso"}