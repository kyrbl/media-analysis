import json
import os
import re
import time

import requests
from bs4 import BeautifulSoup


def download_feeds(website_list_file, output_folder, download_interval):
    # Open the file containing the list of websites
    print(f"Reading list of websites from file: {website_list_file}\n---------------------")
    with open(website_list_file, 'r') as f:
        # Read the list of websites
        websites = f.readlines()

    os.makedirs(output_folder, exist_ok=True)

    # Loop through each website in the list
    print("iterating over websites\n---------------------")
    for website in websites:
        # Remove any trailing whitespace from the website URL
        website = website.strip()
        print(f"Downloading rss feed from website {website}\n")

        # Get a domain name to create readable file names
        domain_name = re.search('https?://([A-Za-z_0-9.-]+).*', website).group(1)
        output_file = f"{output_folder}\\{domain_name}.json"

        # Download the RSS feed from the website
        download_and_save_as_json(website, output_file)

    # Wait for the specified interval before downloading the next set of RSS feeds
    time.sleep(download_interval)


def download_and_save_as_json(url, output_file):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    channels, items = get_channels(soup), get_items(soup)

    data = {
        "feed": channels,
        "items": items
    }

    data = json.dumps(data)

    with open(output_file, 'w') as file:
        file.write(data)


def get_channels(content):
    channels = []
    try:
        result = content.find_all('channel')
        for chan in result:
            title = chan.find('title').text.strip()
            description = chan.find('description').text.strip()
            link = chan.find('link').text.strip()

            data = {
                'title': title,
                'description': description,
                'link': link,
            }

            channels.append(data)
        channels = json.dumps(channels)
        data = json.loads(channels)
        return data
    except Exception as e:
        return e.__doc__


def get_items(content):
    items = []
    try:
        result = content.find_all('item')
        for itm in result:
            title = itm.find('title').text.strip()
            link = itm.find('link').text.strip()
            description = itm.find('description').text.strip()
            published = itm.find('pubDate')
            if published:
                published = published.text.strip()

            data = {
                'title': title,
                'link': link,
                'description': description,
                'published': published,
            }
            items.append(data)
        items = json.dumps(items)
        data = json.loads(items)
        return data
    except Exception as e:
        return e.__doc__
