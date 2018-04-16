from flask import Flask, render_template
import json, requests

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reset')
def reset():
    mapping_config = import_json('data/mapping_config.json')
    headers = {'content-type': 'application/json'}
    delete_response = requests.delete('http://elasticsearch:9200/games', headers=headers)
    print "DELETE: " + str(delete_response.status_code)

    put_response = requests.put('http://elasticsearch:9200/games', headers=headers, data=mapping_config)
    print "PUT: " + str(delete_response.status_code)

    # curl -H 'Content-Type: application/x-ndjson' -XPOST 'elasticsearch:9200/games/doc/_bulk?pretty' --data-binary @games-formatted.import
    game_data = open('data/games-formatted.txt').read()
    put_request = requests.post('http://elasticsearch:9200/games/doc/_bulk', headers={'content-type': 'application/x-ndjson'}, data=game_data)

    return render_template("reset.html", mapping_config=mapping_config, delete_response=delete_response, put_response=put_response, put_request = put_request)


def import_json(filename):
    file_data = open(filename).read()
    json_data = json.loads(file_data)
    return json.dumps(json_data, indent=2, sort_keys=True) # Make it pretty!

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')