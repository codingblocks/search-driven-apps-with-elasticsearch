from flask import Flask, render_template
import json, requests

app = Flask(__name__)
 
@app.route('/')
def hello_whale():
    return render_template("index.html")

@app.route('/reset')
def reset():
    mapping_config = {
        "mappings": {
            "boardgame": {
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "text"},
                    "rating": {"type": "float"},
                    "time": {"type": "integer"},
                    "minimumPlayers": {"type": "integer"},
                    "maximumPlayers": {"type": "integer"},
                    "recommendedPlayers": {"type": "integer"},
                    "mechanics": { "type": "text" },
                    "demo": {"type": "boolean"},
                    "wantsToPlay": {"type": "text"},
                    "owns": {"type": "boolean"},
                    "played": {"type": "boolean"},
                    "boardGameGeekLink": {"type": "text"}
                }
            }
        }
    }

    headers = {'content-type': 'application/json'}
    delete_response = requests.delete('http://elasticsearch:9200/games', headers=headers)
    put_response = requests.put('http://elasticsearch:9200/games', headers=headers, data=json.dumps(mapping_config))

    return render_template("reset.html", mapping_config=mapping_config, delete_response=delete_response, put_response=put_response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')