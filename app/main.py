from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers import analysis_controller, compare_controller, ranking_controller, view_controller

app = FastAPI(
    title="📊 Sistema de Análisis y Ranking",
    description="Plataforma para análisis económico.",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(view_controller.router)
app.include_router(analysis_controller.router)
app.include_router(compare_controller.router)
app.include_router(ranking_controller.router)