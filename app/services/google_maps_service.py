import os
from dotenv import load_dotenv

load_dotenv()

def generate_map(lat, lng):
    key = os.getenv("GOOGLE_MAPS_API_KEY")
    return f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=5&size=400x200&key={key}"