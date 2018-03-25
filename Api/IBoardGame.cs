using System.Collections.Generic;

namespace Api
{
    public interface IBoardGame
    {
      long Id { get; }
      string Title { get; }
      decimal Rating { get; }
      int Time { get; }
      int MinimumPlayers { get; }
      int MaximumPlayers { get; }
      int RecommendedPlayers { get; }
      IEnumerable<string> Mechanics { get; }
      string BoardGameGeekLink { get; }
      IEnumerable<string> WantsToPlay { get; }
  }
}
