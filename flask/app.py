from flask import Flask, render_template
import json, requests

app = Flask(__name__)
 
@app.route('/')
def index():
  search_results = requests.get('http://elasticsearch:9200/games/_search', headers={'content-type': 'application/json'}, data=import_json('data/basic_search.json'))
  results = json.loads(search_results.content) # deserialize the content so we can access things via python
  paging = {
    'showPaging': True,
    'currentPage': 1,
    'startPage': 1,
    'endPage': 10,
    'totalPages': 100
  }
  return render_template("index.j2", hits=results['hits'], aggregations=results['aggregations'], paging=paging)

@app.route('/reset')
def reset():
  responses = {
    'delete': requests.delete('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}),
    'put': requests.put('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}, data=import_json('data/mapping_config.json')),
    'post': requests.post('http://elasticsearch:9200/games/doc/_bulk', headers={'content-type': 'application/x-ndjson'}, data=open('data/games-formatted.txt').read())
  }
  return render_template("reset.j2", responses=responses)

def import_json(filename):
  file_data = open(filename).read()
  json_data = json.loads(file_data)
  return json.dumps(json_data, indent=2, sort_keys=True) # Make it pretty!

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')