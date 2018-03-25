using System.Collections.Generic;

namespace Api
{
  public interface ISearchResult
  {
    IEnumerable<IBoardGame> BoardGames { get; }
    int Total { get; }
  }
}
