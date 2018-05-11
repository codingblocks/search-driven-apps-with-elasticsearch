from flask import Flask, render_template, request
from search import *
from adapters import *
from elasticapm.contrib.flask import ElasticAPM
import os

search_index = os.environ['ELASTICSEARCH_INDEX']

app = Flask(__name__)
apm = ElasticAPM(app, logging=True)

@app.route('/')
def index():
  input_parms = QueryAdapter().url_to_query(request.args)
  search_results = Search(search_index).search(input_parms)
  paging = PagingAdapter().get_paging(request.args, search_results)
  return render_template("index.j2", hits=search_results['hits'], aggregations=search_results['aggregations'], paging=paging)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')