from fastapi import FastAPI
from app.routers.courses import router as router_cursos
from app.routers.students import router as router_estudantes

app = FastAPI()

app.include_router(router=router_cursos, prefix='/api/curso', tags=['curso'])
app.include_router(router=router_estudantes, prefix='/api/estudante', tags=['estudante'])