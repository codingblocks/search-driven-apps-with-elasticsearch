class PagingAdapter:
  def get_paging(self, query_params, search_results):
    size = 12
    current = int(query_params.get('page', 1))
    
    total_hits = int(search_results['hits']['total'])
    total = (total_hits / size) + 1

    if (total_hits % size) != 0:
      total = total + 1

    current = max(1, current)
    current = min(current, total)

    start = max(current - 5, 1)
    end = min(start + 10, total)


    paging = {
      'show': start != end,
      'current': current,
      'start': start,
      'end': end,
      'total': total,
      'size': size
    }

    print('Paging: ' + str(paging))
    return paging