using System.Collections.Generic;
using Api;

namespace ElasticSearch
{
  public class SearchResult : ISearchResult
  {
    public IEnumerable<IBoardGame> BoardGames { get; set; }
    public int Total { get; set; }
  }
}
