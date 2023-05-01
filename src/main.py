from utils import download_and_merge_feeds
from os.path import dirname

MAIN_DIRECTORY = f"{dirname(dirname(__file__))}/data"

# Define the list of websites to download RSS feeds from
WEBSITE_LIST_FILE = f'{MAIN_DIRECTORY}/sites_rss_list.txt'

# Define the interval between RSS feed downloads (in seconds)
DOWNLOAD_INTERVAL = 3600  # Download every hour

# Define the name of the output file for the merged RSS feeds
OUTPUT_FILE = f'{MAIN_DIRECTORY}/merged_rss_feeds.pickle'

while True:
    download_and_merge_feeds(WEBSITE_LIST_FILE, OUTPUT_FILE, DOWNLOAD_INTERVAL)
