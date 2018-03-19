using System.Collections.Generic;

namespace Api
{
  public interface ISearchProvider
  {
    IEnumerable<IBoardGame> Test();
  }
}
