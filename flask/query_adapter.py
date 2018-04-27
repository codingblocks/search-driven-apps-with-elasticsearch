from logger import Logger

class QueryAdapter:
  def url_to_query(self, query_params):
    Logger.info('Parsing query params:' + str(query_params))
    
    wants_to_play = query_params.getlist('wants_to_play')
    mechanics = query_params.getlist('mechanics')

    query = {}
    if wants_to_play or mechanics:
      query['bool'] = { 'filter': [] }

    for p in wants_to_play:
      query['bool']['filter'].append({ 'term': { 'wantsToPlay' : p } })

    for m in mechanics:
      query['bool']['filter'].append({ 'term': { 'mechanics' : m } })

    Logger.info('Parsed query params: ' + str(query))

    return {
      'size': 12,
      'from': (int(query_params.get('page',1)) - 1) * 12,
      'query': query
    }