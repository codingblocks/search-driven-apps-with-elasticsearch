namespace Api
{
  public interface ISearchProvider
  {
    ISearchResult Search(ISearchQuery search);
  }
}
