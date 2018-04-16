from flask import Flask, render_template
import json, requests

app = Flask(__name__)
 
@app.route('/')
def index():
    data = json.dumps({"query": { "match": { "wantsToPlay": "Carrie" } } })
    search_results = requests.get('http://elasticsearch:9200/games/_search', headers={'content-type': 'application/json'}, data=data)
    search_content = json.loads(search_results.content) # deserialize the content so we can access things via python
    return render_template("index.html",search_results=search_results,search_content=search_content)

@app.route('/reset')
def reset():
    responses = {
        'delete': requests.delete('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}),
        'put': requests.put('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}, data=import_json('data/mapping_config.json')),
        'post': requests.post('http://elasticsearch:9200/games/doc/_bulk', headers={'content-type': 'application/x-ndjson'}, data=open('data/games-formatted.txt').read())
    }
    return render_template("reset.html", responses=responses)

def import_json(filename):
    file_data = open(filename).read()
    json_data = json.loads(file_data)
    return json.dumps(json_data, indent=2, sort_keys=True) # Make it pretty!

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')