import json
import pycountry
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="spotify_map")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)

if __name__ == "__main__":
    result = {}

    for country in pycountry.countries:
        try:
            location = geolocator.geocode(country.name)
        except:
            print("Error", country)
            continue

        if not location:
            print(country)
            continue

        result[country.alpha_2] = {
            'longitude': location.longitude,
            'latitude': location.latitude
        }

    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
