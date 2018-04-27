from flask import Flask, render_template, request
from logger import Logger
from search import Search

app = Flask(__name__)

@app.route('/')
def index():
  input_parms = __get_query_from_params()
  results = Search().search(input_parms)
  paging = __get_paging()
  return render_template("index.j2", hits=results['hits'], aggregations=results['aggregations'], paging=paging)

@app.route('/reset')
def reset():
  responses = Search().reset()
  return render_template("reset.j2", game_conversion_success=True, responses=responses)

def __get_query_from_params():
  wants_to_play = request.args.getlist('wants_to_play')
  mechanics = request.args.getlist('mechanics')
  Logger.info(wants_to_play)
  Logger.info(mechanics)
  data = {}
  
  if wants_to_play or mechanics:
    data['bool'] = { 'filter': [] }

  for p in wants_to_play:
    data['bool']['filter'].append({ 'term': { 'wantsToPlay' : p } })

  for m in mechanics:
    data['bool']['filter'].append({ 'term': { 'mechanics' : m } })

  return data

def __get_paging():
  return {
    'showPaging': True,
    'currentPage': 1,
    'startPage': 1,
    'endPage': 10,
    'totalPages': 100
  }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')