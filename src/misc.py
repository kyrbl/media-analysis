from os.path import dirname
from flask import Flask

from libs import connect_to_elastic

DATA_DIR = f"{dirname(dirname(__file__))}\\data"
WEBSITE_LIST_FILE = f'{DATA_DIR}\\sites_rss_list.txt'
ELASTIC_INDEX = 'rss-index'
# Define the interval between RSS feed downloads (in seconds)
DOWNLOAD_INTERVAL = 3600

app = Flask(__name__)
es = connect_to_elastic()
