using System.Collections.Generic;

namespace Api
{
    public interface IBoardGame
    {
      long Id { get; set; }
      string Title { get; set; }
      decimal Rating { get; set; }
      int Time { get; set; }
      int MinimumPlayers { get; set; }
      int MaximumPlayers { get; set; }
      int RecommendedPlayers { get; set; }
      IEnumerable<string> Mechanics { get; set; }
      string BoardGameGeekLink { get; set; }
      bool WantsToPlay { get; set; }
  }
}
