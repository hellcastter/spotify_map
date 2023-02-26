""" Spotify Map """
import json
import pycountry
from flask import render_template, Flask, request
from spotify_api import get_available_markets, get_top_song, search

with open('./countries.json', 'r', encoding='utf-8') as file:
    COUNTRIES = json.load(file)

app = Flask(__name__)

@app.route("/")
def read_root():
    """get index page

    Args:
        request (Request): fastapi request

    Returns:
        _TemplateResponse index.html
    """
    return render_template('index.html')


@app.post("/markets")
async def get_markets():
    """get available markets for the song

    Args:
        request (Request): fastapi request

    Returns:
        list: list of markets
    """
    result = request.json
    artist = result['artist']

    artist_id = await search(artist, 'artist', 1)
    artist_id = artist_id['artists']['items'][0]['id']

    song = get_top_song(artist_id)

    countries = get_available_markets(song['id'])

    response = {
        "name": song['name'],
        "artist": ', '.join([artist['name'] for artist in song['artists']]),
        "url": song['external_urls']['spotify'],
        "countries": []
    }

    for country in countries:
        country_info = pycountry.countries.get(alpha_2=country)

        if not country_info:
            print("NO INFO ABOUT", country)
            continue

        if country_info.alpha_2 not in COUNTRIES:
            print("NO LOCATION: ", country_info)
            continue

        location = COUNTRIES[country_info.alpha_2]

        response['countries'].append({
            'name': country_info.name,
            'flag': country_info.flag,
            'longitude': location['longitude'],
            'latitude': location['latitude']
        })

    return response

if __name__ == "__main__":
    app.run()
