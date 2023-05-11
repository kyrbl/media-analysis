import json
import os

from elasticsearch import helpers


def get_json(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            json_file = os.path.join(folder, filename)
            with open(json_file, 'r') as open_file:
                yield json.load(open_file)


def load_to_elastic(es, folder):
    helpers.bulk(es, get_json(folder), index='my-index')
