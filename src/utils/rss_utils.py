import time

import requests


def download_and_merge_feeds(website_list_file, output_file, download_interval):
    # Open the file containing the list of websites
    print(f"Reading list of websites from file: {website_list_file}\n---------------------")
    with open(website_list_file, 'r') as f:
        # Read the list of websites
        websites = f.readlines()
    print("iterating over websites\n---------------------")
    # Loop through each website in the list
    for website in websites:
        # Remove any trailing whitespace from the website URL
        website = website.strip()
        print(f"Downloading rss feed from website {website}\n")

        # Download the RSS feed from the website
        response = requests.get(website)

        with open(output_file, 'ab') as file:
            file.write(response.content)

    # Wait for the specified interval before downloading the next set of RSS feeds
    time.sleep(download_interval)
