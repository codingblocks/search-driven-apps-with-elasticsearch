using System;
using System.Collections.Generic;

namespace Entities
{
namespace Entities
{
    public class BoardGame
    {
      long Id { get; set; }
      string Game { get; set; }
      decimal Rating { get; set; }
      int time { get; set; }
      int MinPlayers { get; set; }
      int MaxPlayers { get; set; }
      int RecommendedPlayers { get; set; }
      IEnumerable<string> Mechanics { get; set; }
      string BggLink { get; set; }
    }
}
}
