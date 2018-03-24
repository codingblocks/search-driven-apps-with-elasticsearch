docker network create elasticnetwork
docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
docker run -d --name kibana --net elasticnetwork -p 5601:5601 docker.elastic.co/kibana/kibana:6.2.2

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
      "wantsToPlay": {"type": "boolean"},
      "owns": {"type": "boolean"},
      "played": {"type": "boolean"},
      "boardGameGeekLink": {"type": "text"}
   }
  }
 }
}

## https://www.csvjson.com/csv2json
cd /c/Users/joe/OneDrive/Projects/websites/boardgames/Data
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/games/doc/_bulk?pretty' --data-binary @games-formatted.import
