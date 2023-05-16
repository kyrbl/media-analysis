import json
import os

from elasticsearch import helpers, Elasticsearch


def connect_to_elastic():
    return Elasticsearch(
        "http://localhost:9200",
    )


def get_json(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            json_file = os.path.join(folder, filename)
            with open(json_file, 'r', encoding='utf-8') as open_file:
                yield json.load(open_file)


def load_to_elastic(es, folder, index):
    helpers.bulk(es, get_json(folder), index=index)
