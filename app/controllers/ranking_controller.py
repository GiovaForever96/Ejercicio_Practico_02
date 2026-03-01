from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.country_service import get_all_countries
from app.utils.risk_engine import calculate_risk

router = APIRouter(prefix="/ranking", tags=["Ranking"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def ranking_view(request: Request):

    countries = get_all_countries()

    ranking_list = []

    for c in countries:

        population = c.get("population") or 0
        area = c.get("area") or 1

        if area == 0:
            area = 1

        density = population / area

        score, level, badge = calculate_risk(population, density)

        ranking_list.append({
            "name": c.get("name", "Unknown"),
            "population": population,
            "score": score,
            "level": level,
            "flag": c.get("flag", ""),
            "badge": badge
        })

    # ordenar por población descendente
    ranking_list.sort(key=lambda x: x["population"], reverse=True)

    # top 10
    ranking_list = ranking_list[:10]

    return templates.TemplateResponse(
        "ranking.html",
        {
            "request": request,
            "ranking": ranking_list
        }
    )