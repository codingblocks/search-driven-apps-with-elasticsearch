from flask import Flask, render_template, request
from search import *
from adapters import *
import os

search_index = os.environ['ELASTICSEARCH_INDEX']

app = Flask(__name__)

@app.route('/')
def index():
  input_parms = QueryAdapter().url_to_query(request.args)
  search_results = Search(search_index).search(input_parms)
  paging = PagingAdapter().get_paging(request.args, search_results)
  return render_template("index.j2", hits=search_results['hits'], aggregations=search_results['aggregations'], paging=paging)

@app.route('/reset')
def reset():
  responses = Search(search_index).reset()
  return render_template("reset.j2", conversion_success=True, responses=responses)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')