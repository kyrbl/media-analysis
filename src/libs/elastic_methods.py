from elasticsearch import Elasticsearch


def connect_to_elastic():
    return Elasticsearch(
        "http://localhost:9200",
    )
