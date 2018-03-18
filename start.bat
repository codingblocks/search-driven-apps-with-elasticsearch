docker network create elasticnetwork
docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
docker run -d --name kibana --net elasticnetwork -p 5601:5601 docker.elastic.co/kibana/kibana:6.2.2



curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/games/doc/_bulk?pretty' --data-binary @games.json
curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/games/doc/_bulk?pretty' --data-binary @games.json



## https://www.csvjson.com/csv2json
$ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/games/doc/_bulk?pretty' --data-binary @games-formatted.import





{"index":{"_index":"shakespeare","_id":0}}
{"type":"act","line_id":1,"play_name":"Henry IV", "speech_number":"","line_number":"","speaker":"","text_entry":"ACT I"}


PUT /games
{
 "mappings": {
  "doc": {
   "properties": {
      "ID": {"type": "integer"},
      "GAME": {"type": "keyword"},
      "RATING": {"type": "float"},
      "TIME": {"type": "integer"},
      "MIN PLAYERS": {"type": "integer"},
      "MAX PLAYERS": {"type": "integer"},
      "REC PLAYERS": {"type": "integer"},
      "MECHANICS": {"type": "keyword"},
      "DEMO": {"type": "boolean"},
      "WANTS TO PLAY": {"type": "boolean"},
      "OWNS": {"type": "boolean"},
      "PLAYED": {"type": "boolean"},
      "BGG LINK": {"type": "text"}
   }
  }
 }
}