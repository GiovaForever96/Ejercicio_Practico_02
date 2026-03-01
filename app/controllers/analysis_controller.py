from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.country_service import get_country
from app.services.google_maps_service import generate_map
from app.utils.risk_engine import calculate_risk

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/analysis-result")
def analysis_result(request: Request, country: str):

    data = get_country(country)

    if not data:
        return templates.TemplateResponse(
            "analysis.html",
            {
                "request": request,
                "error": "Country not found. Please try again."
            }
        )

    density = data["population"] / data["area"]
    score, level, badge = calculate_risk(data["population"], density)

    map_url = generate_map(data["latlng"][0], data["latlng"][1])
    print("map_url",map_url)

    return templates.TemplateResponse(
        "analysis.html",
        {
            "request": request,
            "country_data": {
                "name": data["name"],
                "population": data["population"],
                "region": data["region"],
                "currency": data["currency"],
                "flag": data["flag"],
                "map": map_url,
                "score": score,
                "level": level,
                "badge": badge
            }
        }
    )