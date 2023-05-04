from utils import download_feeds, convert_all_xmls_to_jsons
from os.path import dirname

DATA_DIR = f"{dirname(dirname(__file__))}\\data"

# Define the list of websites to download RSS feeds from
WEBSITE_LIST_FILE = f'{DATA_DIR}\\sites_rss_list.txt'
XML_OUTPUT_FOLDER = f'{DATA_DIR}\\xmls'
JSON_OUTPUT_FOLDER = f'{DATA_DIR}\\jsons'

# Define the interval between RSS feed downloads (in seconds)
DOWNLOAD_INTERVAL = 3600  # Download every hour

# Define the name of the output file for the merged RSS feeds

if __name__ == "__main__":
    print(f"Starting to download rss feeds with an interval of {DOWNLOAD_INTERVAL} seconds")
    # while True:
    download_feeds(WEBSITE_LIST_FILE, XML_OUTPUT_FOLDER, DOWNLOAD_INTERVAL)
    convert_all_xmls_to_jsons(XML_OUTPUT_FOLDER, JSON_OUTPUT_FOLDER)
