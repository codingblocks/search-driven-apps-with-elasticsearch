using System.Collections.Generic;
using Api;

namespace ElasticSearch
{
    internal class BoardGame : IBoardGame
    {
      public long Id { get; set; }
      public string Title { get; set; }
      public decimal Rating { get; set; }
      public int Time { get; set; }
      public int MinimumPlayers { get; set; }
      public int MaximumPlayers { get; set; }
      public int RecommendedPlayers { get; set; }
      public IEnumerable<string> Mechanics { get; set; }
      public string BoardGameGeekLink { get; set; }
      public bool WantsToPlay { get; set; }
    }
}
