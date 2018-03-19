docker network create elasticnetwork
docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
docker run -d --name kibana --net elasticnetwork -p 5601:5601 docker.elastic.co/kibana/kibana:6.2.2

DELETE /games
PUT /games
{
 "mappings": {
  "boardgame": {
   "properties": {
      "Id": {"type": "integer"},
      "title": {"type": "text"},
      "Rating": {"type": "float"},
      "Time": {"type": "integer"},
      "MinimumPlayers": {"type": "integer"},
      "MaximumPlayers": {"type": "integer"},
      "RecommendedPlayers": {"type": "integer"},
      "Mechanics": { "type": "text" },
      "Demo": {"type": "boolean"},
      "WantsToPlay": {"type": "boolean"},
      "Owns": {"type": "boolean"},
      "Played": {"type": "boolean"},
      "BoardGameGeekLink": {"type": "text"}
   }
  }
 }
}

## https://www.csvjson.com/csv2json
cd /c/Users/joe/OneDrive/Projects/websites/boardgames/Data
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/games/doc/_bulk?pretty' --data-binary @games-formatted.import
