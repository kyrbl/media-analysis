from src import rss_utils

# Define the list of websites to download RSS feeds from
WEBSITE_LIST_FILE = 'data/sites_rss_list.txt'

# Define the interval between RSS feed downloads (in seconds)
DOWNLOAD_INTERVAL = 3600  # Download every hour

# Define the name of the output file for the merged RSS feeds
OUTPUT_FILE = 'data/merged_rss_feeds.pickle'

while True:
    rss_utils.download_and_merge_feeds(WEBSITE_LIST_FILE, OUTPUT_FILE, DOWNLOAD_INTERVAL)
