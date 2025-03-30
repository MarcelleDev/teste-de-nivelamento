from fastapi import FastAPI
from api import router

app = FastAPI(
    title="API de Operadoras",
    description="API para buscar operadoras de saúde pelo nome ou razão social.",
    version="1.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
def status():
    return {"message": "API Online! Acesse /api/buscar?termo=XYZ"}
