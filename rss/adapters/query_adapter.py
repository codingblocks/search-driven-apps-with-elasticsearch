class QueryAdapter:
  def url_to_query(self, query_params):
    print('Parsing query params:' + str(query_params))
    
    tags = query_params.getlist('tags')
    search = query_params.get('search')

    query = {}
    if tags:
      query['bool'] = { 'filter': [] }

    for t in tags:
      query['bool']['filter'].append({ 'term': { 'tags.keyword' : t } })

    if search:
      query['fuzzy'] = { 'title': search }

    print('Parsed query params: ' + str(query))

    return {
      'size': 20,
      'from': (int(query_params.get('page',1)) - 1) * 20,
      'query': query
    }