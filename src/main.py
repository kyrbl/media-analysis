import time
from threading import Thread
from misc import *

from libs import download_feeds, load_to_elastic
from apis import *


def update_feeds():
    while True:
        es.delete_by_query(index=ELASTIC_INDEX, body={"query": {"match_all": {}}})
        print(f"Starting to download rss feeds with an interval of {DOWNLOAD_INTERVAL} seconds")
        download_feeds(WEBSITE_LIST_FILE, JSON_OUTPUT_FOLDER)
        print("Loading jsons to Elastic.")
        load_to_elastic(es, JSON_OUTPUT_FOLDER, ELASTIC_INDEX)
        print("Successfully loaded.")
        time.sleep(DOWNLOAD_INTERVAL)


if __name__ == "__main__":
    app_thread = Thread(target=app.run)
    app_thread.start()
    update_feeds()
