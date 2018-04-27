import json, requests

class Importer:

  def convert_json_to_elastic(self, input_file_name, output_file_name):
    games = self.get_games(input_file_name)
    rows = self.games_to_rows(games)
    self.write_games(rows, output_file_name)
    return len(rows) / 2

  def get_games(self, input_file_name):
    with open(input_file_name) as input_file:
      file_data = input_file.read()
    return json.loads(file_data)

  def games_to_rows(self, games):
    output_rows = []
    counter = 1
    for game in games:
      header_row = '{"index":{"_index":"games", "_type":"boardgame", "_id": "' + str(counter) +'"}}'
      counter += 1
      output_rows.append(header_row)
    
      game_row = json.dumps(game)
      output_rows.append(game_row)

      return output_rows

  def write_games(self, output_rows, output_file_name):
    with open(output_file_name, 'w') as output_file:
      for row in output_rows:
        output_file.write("%s\n" % row)