import requests


def get_umpire(game_id, api_key):
    umpire_url = f'http://api.sportradar.us/mlb/trial/v6.5/en/games/{game_id}/summary.json?api_key={api_key}'
    resp = requests.get(umpire_url).json()
    officials = resp['game']['officials']
    for official in officials:
        if official['assignment'] == 'HP':
            return official['full_name']
