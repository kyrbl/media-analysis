import re
import os
import requests


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
        output_file = f"{output_folder}\\{domain_name}.xml"

        # Download the RSS feed from the website
        response = requests.get(website)

        with open(output_file, 'wb') as file:
            file.write(response.content)

    # Wait for the specified interval before downloading the next set of RSS feeds
    # time.sleep(download_interval)
