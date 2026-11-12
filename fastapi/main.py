from fastapi import FastAPI
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Curso de Python",
        "aulas": 10,
        "horas": 100
    },
    2: {
        "titulo": "Curso de JavaScript",
        "aulas": 20,
        "horas": 200
    }
}


@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    return cursos[curso_id]

@app.post("/cursos")
async def post_curso(curso: Curso):
    return cursos[curso.id]

@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    return cursos[curso_id]

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    return cursos[curso_id]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
