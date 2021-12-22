import requests
import os

def fetch_auth_token(cli_token: str):
    url = "{0}/cli-tokens/{1}".format(os.environ.get("API_URL"), cli_token)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
