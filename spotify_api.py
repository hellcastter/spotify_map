""" help functions """
import os
import json
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token() -> str:
    """get spotify token

    Returns:
        str: token

    >>> isinstance(get_token, str)
    True
    """
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data, timeout=10000)
    json_result = json.loads(result.content)
    return json_result['access_token']

def get_headers(token: str) -> dict:
    """get headers

    Args:
        token (str): spotify token

    Returns:
        dict: all headers
    """
    return {"Authorization": f"Bearer {token}"}

def get(endpoint: str, query="") -> dict:
    """method to get info

    Args:
        endpoint (str): url
        query (str, optional): Defaults to "".

    Returns:
        dict: response
    """
    headers = get_headers( get_token() )

    url = endpoint + query
    response = requests.get(url, headers=headers, timeout=10000)
    return json.loads(response.content)

async def search(query: str, q_type: str, limit=10):
    """search method

    Args:
        token (str): spotify token
        query (str): what to search
        q_type (str): type of search
        limit (int, optional): Defaults to 10.
    """
    endpoint = "https://api.spotify.com/v1/search"
    query = f"?q={query}&type={q_type}&limit={limit}"

    return get(endpoint, query)

def get_top_song(artist_id: str) -> str:
    """get top tracks

    Args:
        artist_id (str): artist id
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    query = "?market=UA"
    top_tracks = get(url, query)

    top_track_id = top_tracks['tracks'][0]

    return top_track_id


def get_available_markets(song_id: str) -> list:
    """get available markets for songs

    Args:
        song_id (str): song id

    Returns:
        list: list of countries codes
    """
    url = f"https://api.spotify.com/v1/tracks/{song_id}/"
    song = get(url)

    return song['available_markets']
