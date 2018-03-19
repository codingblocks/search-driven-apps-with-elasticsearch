using System;
using System.Collections.Generic;

namespace Entities
{
    public class BoardGame
    {
      public long Id { get; set; }
      public string Game { get; set; }
      public decimal Rating { get; set; }
      public int time { get; set; }
      public int MinPlayers { get; set; }
      public int MaxPlayers { get; set; }
      public int RecommendedPlayers { get; set; }
      public IEnumerable<string> Mechanics { get; set; }
      public string BoardGameGeek { get; set; }
    }
}