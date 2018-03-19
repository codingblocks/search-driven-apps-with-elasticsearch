using System.Collections.Generic;
using Api;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Website.Pages
{
    public class IndexModel : PageModel
    {
      public IndexModel(ISearchProvider searchProvider)
      {
        SearchProvider = searchProvider;
      }

      private ISearchProvider SearchProvider { get; set; }
      public IEnumerable<IBoardGame> GamesToPlay;
        public void OnGet()
        {
          GamesToPlay = SearchProvider.Test();
        }
    }
}
