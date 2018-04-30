from importer import Importer
import json, requests

class Search:

  def search(self, params = {}):
    basic_search = self.__import_dict('data/basic_search.json')
    if params['query']:
      basic_search['query'] = params['query']
    
    basic_search['size'] = params['size']
    basic_search['from'] = params['from']

    return self.__get(basic_search)

  def reset(self):
    games_converted = Importer().convert_json_to_elastic('data/games.json','data/games-formatted.import')
    responses = {
      'delete': requests.delete('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}),
      'put': requests.put('http://elasticsearch:9200/games', headers={'content-type': 'application/json'}, data=self.__import_json('data/mapping_config.json')),
      'post': requests.post('http://elasticsearch:9200/games/doc/_bulk', headers={'content-type': 'application/x-ndjson'}, data=open('data/games-formatted.txt').read())
    }
    return responses

  def __get(self, dict):
    query = self.__format(dict)
    print('/GET')
    print(query)

    results = requests.get('http://elasticsearch:9200/games/_search', headers={'content-type': 'application/json'}, data=query)
    
    print('/Response: ' + str(results.status_code))
    
    results = json.loads(results.content)
    print(self.__format(results))

    return results

  def __format(self, data):
    return json.dumps(data, indent=2, sort_keys=True)

  def __import_dict(self, filename):
    file_data = open(filename).read()
    return json.loads(file_data)

  def __import_json(self, filename):
    json_data = self.__import_dict(filename)
    return json.dumps(json_data, indent=2, sort_keys=True) # Make it pretty!