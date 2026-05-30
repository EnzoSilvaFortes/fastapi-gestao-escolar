from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Curso(Base):
    __tablename__ = 'cursos'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    carga_horaria: Mapped[int]
    ativo: Mapped[bool] = mapped_column(default=True)
    
    # Relacionamento para a entidade de Estudantes
    estudantes: Mapped[list["Estudante"]] = relationship(back_populates="curso", cascade="all, delete-orphan")
    
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )