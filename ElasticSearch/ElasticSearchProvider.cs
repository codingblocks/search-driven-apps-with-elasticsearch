using System;
using Api;
using Nest;

namespace ElasticSearch
{
  public class ElasticSearchProvider : ISearchProvider
  {
    public ISearchResult Search(ISearchQuery search)
    {
      // TODO
      var settings = new ConnectionSettings(new Uri("http://localhost:9200")).DefaultIndex("games");

      var client = new ElasticClient(settings);
      var searchResponse = client.Search<BoardGame>(s => s
        .From(Math.Max(0, search.PageNumber - 1) * search.PageSize) // TODO
        .Size(search.PageSize)
      );
      return new SearchResult
      {
        BoardGames = searchResponse.Documents,
        Total = (int) searchResponse.Total // Don't expect anything near max int
      };
    }
  }
}
