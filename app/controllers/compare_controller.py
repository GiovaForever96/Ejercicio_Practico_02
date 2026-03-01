from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.country_service import get_country
from app.utils.risk_engine import calculate_risk

router = APIRouter(prefix="/compare", tags=["Comparison"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def compare(request: Request, country1: str = None, country2: str = None):

    result = None
    error = None

    if country1 and country2:

        c1 = get_country(country1)
        c2 = get_country(country2)

        if not c1 or not c2:
            error = "One country not found"
        else:
            d1 = c1["population"] / c1["area"]
            d2 = c2["population"] / c2["area"]

            s1, l1, b1 = calculate_risk(c1["population"], d1)
            s2, l2, b2 = calculate_risk(c2["population"], d2)

            winner = c1["name"] if s1 < s2 else c2["name"]

            result = {
                        "country1": {
                            "name": c1["name"],
                            "score": s1,
                            "level": l1,
                            "flag": c1["flag"],
                            "badge": b1
                        },
                        "country2": {
                            "name": c2["name"],
                            "score": s2,
                            "level": l2,
                            "flag": c2["flag"],
                            "badge": b2
                        },
                        "winner": winner
                    }

    return templates.TemplateResponse(
        "compare.html",
        {
            "request": request,
            "result": result,
            "error": error
        }
    )