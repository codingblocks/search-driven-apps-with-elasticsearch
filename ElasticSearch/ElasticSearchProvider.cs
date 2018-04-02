using System;
using System.Linq;
using Api;
using Nest;

namespace ElasticSearch
{
  public class ElasticSearchProvider : ISearchProvider
  {
    public ISearchResult Search(ISearchQuery search)
    {
      // TODO
      var settings = new ConnectionSettings(new Uri("http://elasticsearch:9200")).DefaultIndex("games");

      var client = new ElasticClient(settings);

      ISearchResponse<BoardGame> searchResponse;
      // TODO OMG
      if (search.WantsToPlay != null && search.WantsToPlay.Any())
      {
        searchResponse = client.Search<BoardGame>(s => s
          .From(Math.Max(0, search.PageNumber - 1) * search.PageSize) // TODO
          .Size(search.PageSize)
          .Query(q => q
              .Match(c => c
                .Field(p => p.WantsToPlay)
                .Query(search.WantsToPlay.First()))
            )
          // TODO How to Multiple?
          //  .Query(q => q
          //q.Term("name", "Nest")
          //  || q.Term("name", "Elastica")
          //  )
        );
      }
      else
      {
        searchResponse = client.Search<BoardGame>(s => s
          .From(Math.Max(0, search.PageNumber - 1) * search.PageSize) // TODO
          .Size(search.PageSize)
        );
      }

      return new SearchResult
      {
        BoardGames = searchResponse.Documents,
        Total = (int) searchResponse.Total // Don't expect anything near max int
      };
    }
  }
}
