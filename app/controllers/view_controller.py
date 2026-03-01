from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/analysis-view")
def analysis_view(request: Request):
    return templates.TemplateResponse("analysis.html", {"request": request})

@router.get("/compare-view")
def compare_view(request: Request):
    return templates.TemplateResponse("compare.html", {"request": request})

@router.get("/ranking-view")
def ranking_view(request: Request):
    return templates.TemplateResponse("ranking.html", {"request": request})