import requests

def get_country(country: str):

    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    return {
        "name": data["name"]["common"],
        "population": data["population"],
        "region": data["region"],
        "area": data["area"],
        "currency": list(data["currencies"].keys())[0],
        "flag": data["flags"]["png"],
        "latlng": data["latlng"]
    }

def get_all_countries():

    url = "https://restcountries.com/v3.1/all?fields=name,population,area,flags,region"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    countries = []

    for c in data:
        countries.append({
            "name": c.get("name", {}).get("common", "Unknown"),
            "population": c.get("population", 0),
            "area": c.get("area", 1),  # evitar None
            "flag": c.get("flags", {}).get("png", ""),
            "region": c.get("region", "Unknown")
        })

    return countries