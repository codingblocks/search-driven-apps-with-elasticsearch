using System.Collections.Generic;

namespace Api
{
  public interface ISearchQuery
  {
    int PageNumber { get; }
    int PageSize { get; }
    string Title { get; }
    decimal MinimumRating { get; }
    int MinimumPlayers { get; }
    int MaximumPlayers { get; }
    int RecommendedPlayers { get; }
    IEnumerable<string> Mechanics { get; }
    IEnumerable<string> WantsToPlay { get; }
  }
}
