from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    idade: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    
    # Relacionamento reverso com Curso
    curso: Mapped["Curso"] = relationship(back_populates="estudantes")
    
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )