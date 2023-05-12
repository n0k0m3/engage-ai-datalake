import requests
import os
import time

COUNTRY_URL = "http://api.worldbank.org/v2/country?format=json&per_page=500"
FILE_URL = "https://api.worldbank.org/v2/en/country/{}?downloadformat=csv"


def download_data(url, id):
    while True:
        response = requests.get(url.format(id))
        # If response contains "Request Error", wait 5 seconds and try again
        if "Request Error" in response.text:
            time.sleep(5)
            continue
        break
    with open(f"./data/{id}.zip", "wb") as f:
        f.write(response.content)


def get_countries_ids(country_url):
    # Get all countries from the World Bank API
    response = requests.get(country_url)
    countries = response.json()[1]
    # get all countries ids that are not aggregates
    return [
        country["id"]
        for country in countries
        if country["region"]["value"] != "Aggregates"
    ]


def download_all_data():
    # Download data files from the World Bank API
    os.makedirs("./data", exist_ok=True)
    country_ids = get_countries_ids(COUNTRY_URL)
    while True:
        ids = [file.split(".")[0] for file in os.listdir("./data")]
        diff = set(country_ids) - set(ids)
        if len(diff) == 0:
            break
        for id in diff:
            if os.path.isfile(f"./data/{id}.zip"):
                continue
            download_data(FILE_URL, id)
