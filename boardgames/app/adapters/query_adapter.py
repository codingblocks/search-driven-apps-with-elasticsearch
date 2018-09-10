class QueryAdapter:
  def url_to_query(self, query_params):
    print('Parsing query params:' + str(query_params))
    
    wants_to_play = query_params.getlist('wants_to_play')
    mechanics = query_params.getlist('mechanics')
    time_ranges = query_params.get('time_ranges')

    query = {}
    if wants_to_play or mechanics:
      query['bool'] = { 'filter': [] }

    for p in wants_to_play:
      query['bool']['filter'].append({ 'term': { 'wantsToPlay' : p } })

    for m in mechanics:
      query['bool']['filter'].append({ 'term': { 'mechanics' : m } })

    if time_ranges:
      query['range'] = {
        'time': {}
      }
      query_parts = time_ranges.split('-')
      query['range']['time']['gte'] = query_parts[0]
      query['range']['time']['lte'] = query_parts[1]

    print('Parsed query params: ' + str(query))

    return {
      'size': 12,
      'from': (int(query_params.get('page',1)) - 1) * 12,
      'query': query
    }