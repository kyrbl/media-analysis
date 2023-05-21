import json
import re
from datetime import datetime

import pytz
import requests
from bs4 import BeautifulSoup


def read_feeds_and_load_to_elastic(website_list_file, es, index):
    # Open the file containing the list of websites
    print(f"Reading list of websites from file: {website_list_file}\n---------------------")
    with open(website_list_file, 'r') as f:
        # Read the list of websites
        websites = f.readlines()

    # Loop through each website in the list
    print("iterating over websites\n---------------------")
    for website in websites:
        website = website.strip()
        print(f"Reading rss feed from website {website}\n")

        nodes = read_feed(website)
        for node in nodes:
            es.index(index=index, document=node)


def read_feed(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    channels, items = get_channel(soup), get_items(soup)

    data = [channels | item for item in items]
    return data


def get_channel(content):
    try:
        result = content.find_all('channel')
        chan = result[0]

        title = chan.find('title').text.strip()
        description = chan.find('description').text.strip()
        link = chan.find('link').text.strip()

        data = {
            'feed_title': title,
            'feed_description': description,
            'feed_link': link,
        }
        data = json.dumps(data)

        return json.loads(data)
    except Exception as e:
        return e.__doc__


def convert_date_to_utc(date):
    pattern = r"\b[A-Za-z]{3}, \d{2} [A-Za-z]{3} \d{4} \d{2}:\d{2}:\d{2} [+-]\d{4}\b"
    match = re.search(pattern, str(date))

    if match:
        extracted_date = match.group(0)

    date_obj = datetime.strptime(extracted_date, '%a, %d %b %Y %H:%M:%S %z')
    utc_timezone = pytz.timezone('UTC')
    utc_date = date_obj.astimezone(utc_timezone)
    return utc_date.strftime('%Y-%m-%d'), utc_date.strftime('%H:%M:%S')


def get_items(content):
    items = []
    try:
        result = content.find_all('item')
        for itm in result:
            title = itm.find('title').text.strip()
            link = itm.find('link').text.strip()
            description = itm.find('description').text.strip()
            published = itm.find('pubdate')
            if published:
                published_date, published_time = convert_date_to_utc(published)
            else:
                published_date, published_time = "NaN", "NaN"

            data = {
                'item_title': title,
                'item_link': link,
                'item_description': description,
                'published_date': published_date,
                'published_time': published_time,
            }
            items.append(data)
        items = json.dumps(items)
        data = json.loads(items)
        return data
    except Exception as e:
        return e.__doc__
