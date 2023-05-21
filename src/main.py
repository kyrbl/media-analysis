import time
from threading import Thread
from misc import *

from libs import read_feeds_and_load_to_elastic
from apis import *


def update_feeds():
    while True:
        print(f"Starting to download rss feeds with an interval of {DOWNLOAD_INTERVAL} seconds")
        read_feeds_and_load_to_elastic(WEBSITE_LIST_FILE, es, ELASTIC_INDEX)
        print(f"Sleeping for {DOWNLOAD_INTERVAL} seconds.")
        time.sleep(DOWNLOAD_INTERVAL)


if __name__ == "__main__":
    # app_thread = Thread(target=app.run)
    # app_thread.start()
    update_feeds()
