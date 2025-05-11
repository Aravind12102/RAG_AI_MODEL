import requests

def define(term: str) -> str:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{term}"
    response = requests.get(url)
    if response.status_code == 200:
        definition = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        return definition
    return "Definition not found"
