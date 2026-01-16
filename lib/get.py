import requests
import json


def all_locations():
    """Fetch and return all locations from the JSON API."""
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
    response = requests.get(url)
    json_content = json.loads(response.text)
    return json_content


def all_people():
    """Fetch and return all people from the JSON API."""
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    response = requests.get(url)
    json_content = json.loads(response.text)
    return json_content

