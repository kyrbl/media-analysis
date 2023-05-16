from misc import app, es, ELASTIC_INDEX
from flask import jsonify, request, render_template

import json


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/get_feed', methods=['GET', 'POST'])
def get_user():
    query = json.loads(request.form['query'])
    # Perform Elasticsearch search based on the query
    search_results = es.search(index=ELASTIC_INDEX, query=query)

    # Process the search results
    hits = search_results['hits']['hits']
    results = [hit['_source'] for hit in hits]

    # Return the search results to the user
    return render_template('results.html', results=results)
