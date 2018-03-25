using System;
using System.Collections.Generic;
using Api;
using ElasticSearch;
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
    public int CurrentPage { get; set; }
    public int TotalPages { get; set; }
    public int TotalCount { get; set; }
    public int PageSize { get; set; } = 12;
    public int PagingToolbarEnd { get; set; }
    public int PagingToolbarStart { get; set; }
    public bool ShowPagingToolbar { get; set; }

    public void OnGet()
    {
      ParseInput();
      var results = Search(); // TODO this is also parses input :(
      GamesToPlay = results.BoardGames;
      TotalCount = results.Total;
      CalculatePaging(results);
    }

    private void ParseInput()
    {
      var pageInput = HttpContext.Request.Query["page"];
      CurrentPage = int.TryParse(pageInput, out var currentPage) ? currentPage : 1;
    }

    private void CalculatePaging(ISearchResult results)
    {
      if (PageSize == 0)
      {
        TotalPages = 0;
        PagingToolbarStart = 1;
        PagingToolbarEnd = 0;
        ShowPagingToolbar = false;
        return;
      }
      TotalPages = (int) Math.Ceiling(Decimal.Divide(results.Total, PageSize));
      PagingToolbarStart = Math.Max(1, CurrentPage - 3);
      PagingToolbarEnd = Math.Min(TotalPages, PagingToolbarStart + 4);
      ShowPagingToolbar = PagingToolbarStart != PagingToolbarEnd;
    }

    private ISearchResult Search()
    {
      var query = new BoardGameSearch
      {
          PageSize = PageSize,
          PageNumber = CurrentPage
      };

      var results = SearchProvider.Search(query);

      return results;
    }
  }
}
