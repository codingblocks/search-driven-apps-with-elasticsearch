using System;
using System.Collections.Generic;
using Api;
using Nest;

namespace ElasticSearch
{
  public class ElasticSearchProvider : ISearchProvider
  {
    public IEnumerable<IBoardGame> Test()
    {
      var settings = new ConnectionSettings(new Uri("http://localhost:9200"))
        .DefaultIndex("games");

      var client = new ElasticClient(settings);
      var searchResponse = client.Search<BoardGame>(s => s
        .From(0)
        .Size(20)
        .Query(q => q
          .Term(p => p.WantsToPlay, true)
      ));
      return searchResponse.Documents;
    }
  }
}
