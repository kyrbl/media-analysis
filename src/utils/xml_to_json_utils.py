import datetime
import re
import xmltodict
import json
import os


def convert_xml_to_json(in_file, out_file):
    file = open(in_file, "r", errors="ignore")
    text = file.read()
    file.close()

    rss = text.split('\n')
    text = ""
    for i in range(len(rss)):
        text = text + " " + rss[i]
    text = re.sub('^\s', '', text)

    title = re.findall('<title>(.+?)<\/title>', text)
    source = title[0]
    source = re.sub('[\s\-]*$', '', source)
    source = re.sub('"', '\"', source)

    description = re.findall('<description>(.*?)<\/description>', text)
    link = re.findall('<link>(.+?)<\/link>', text)
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%dT%H:%M:00Z")

    for i in range(1, len(title) - 1):
        description[i] = re.sub('[\s\-]*$', '', description[i])
        description[i] = re.sub('"', '\"', description[i])
        description[i] = re.sub('&', '&amp;', description[i])

        with open(out_file, "a") as json_file:
            json_file.write("{\n\"title\":\"" + title[i] + "\",")
            json_file.write("\"textBody\":\"" + description[i] + "\",")
            json_file.write("\"source\":\"" + source + "\",")
            json_file.write("\"PubDate\":\"" + formatted_time + "\",")
            json_file.write("\"URL\":\"" + link[i] + "\"\n}")

            if i < len(title) - 2:
                json_file.write(",")


def convert_all_xmls_to_jsons(xml_folder, json_folder):
    os.makedirs(json_folder, exist_ok=True)
    for filename in os.listdir(xml_folder):
        xml_file = os.path.join(xml_folder, filename)
        json_file = os.path.join(json_folder, filename[:-4] + ".json")
        convert_xml_to_json(xml_file, json_file)
