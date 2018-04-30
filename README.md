# For Dev:

```// This will spin up elasticsearch and kibana
docker-compose -f docker-compose-dev.yml up```

```docker build -t flask:latest .```
```docker-compose up -d; docker logs -f website```


## Bugs
* Paging not keeping params
* Redo UI
* Filter on reset page

Production:
* kompose convert -f production.yml

## Questions...

Why does this seem wrong?
If I use docker-compose up and python crashes, I have to restart everything?

```Useful queries:
# Mappings
DELETE /games
PUT /games
{
 "mappings": {
  "boardgame": {
   "properties": {
      "id": {"type": "integer"},
      "title": {"type": "text"},
      "rating": {"type": "float"},
      "time": {"type": "integer"},
      "minimumPlayers": {"type": "integer"},
      "maximumPlayers": {"type": "integer"},
      "recommendedPlayers": {"type": "integer"},
      "mechanics": { "type": "text" },
      "demo": {"type": "boolean"},
      "wantsToPlay": { "type": "keyword" },
      "owns": {"type": "boolean"},
      "played": {"type": "boolean"},
      "boardGameGeekLink": {"type": "text"}
   }
  }
 }
}
# Make sure the search is there..
GET /games
# Search via match (don't do this)
GET /games/_search
{
  "query": {
    "match": { 
      "wantsToPlay": "Carrie" }
  }
}
# Get just one
GET /games/_search
{
    "query": {
      "term" : {
          "wantsToPlay" : "Josh"
      }
    }
}
# UNION
GET /games/_search
{
    "query": {
      "terms" : {
          "wantsToPlay" : ["Josh","Carrie"]
      }
    }
}
# INTERSECTION
GET /games/_search
{
    "query": {
    "bool": {
      "filter": [
        { "term": { "wantsToPlay" : "Josh" } },
        { "term": { "wantsToPlay" : "Carrie" } }
      ]
    }
  }
}
# Aggregates, the entire matrix
POST /games/_search?size=0
{
  "size": 0,
  "aggs" : {
    "interactions" : {
      "adjacency_matrix" : {
        "filters" : {
          "Josh" : { "term": { "wantsToPlay" : "Josh" } },
          "Carrie" : { "term": { "wantsToPlay" : "Carrie" } },
          "Joe" : { "term": { "wantsToPlay" : "Joe" } }
        }
      }
    }
  }
}
# Aggregations
GET /_search
{
    "aggs" : {
        "genres" : {
            "terms" : { "field" : "wantsToPlay" }
        }
    }
}```