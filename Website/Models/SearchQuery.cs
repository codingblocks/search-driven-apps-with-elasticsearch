using System.Collections.Generic;
using Api;

namespace Website.Models
{
    public class SearchQuery : ISearchQuery
    {
      public int PageNumber { get; set; } = 1;
      public int PageSize { get; set; } = 20;
      public string Title { get; set; }
      public decimal MinimumRating { get; set; }
      public int MinimumPlayers { get; set; }
      public int MaximumPlayers { get; set; }
      public int RecommendedPlayers { get; set; }
      public IEnumerable<string> Mechanics { get; set; }
      public IEnumerable<string> WantsToPlay { get; set; }
  }
}
