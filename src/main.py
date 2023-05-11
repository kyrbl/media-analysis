from elasticsearch import Elasticsearch

from utils import download_feeds, load_to_elastic
from os.path import dirname

DATA_DIR = f"{dirname(dirname(__file__))}\\data"

WEBSITE_LIST_FILE = f'{DATA_DIR}\\sites_rss_list.txt'
XML_OUTPUT_FOLDER = f'{DATA_DIR}\\xmls'
JSON_OUTPUT_FOLDER = f'{DATA_DIR}\\jsons'

# Define the interval between RSS feed downloads (in seconds)
DOWNLOAD_INTERVAL = 3600

if __name__ == "__main__":
    client = Elasticsearch(
        "http://localhost:9200",
    )

    while True:
        print(f"Starting to download rss feeds with an interval of {DOWNLOAD_INTERVAL} seconds")
        download_feeds(WEBSITE_LIST_FILE, JSON_OUTPUT_FOLDER, DOWNLOAD_INTERVAL)
        print("Loading jsons to Elastic.")
        load_to_elastic(client, JSON_OUTPUT_FOLDER)
        print("Successfully loaded.")
