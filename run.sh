# docker network create elasticnetwork
# docker build -t boardgames .
# docker run -d -p 8080:80 --name boardgames boardgames
# docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
# docker run -d --name kibana --net elasticnetwork -p 5601:5601 docker.elastic.co/kibana/kibana:6.2.2

docker-compose down
docker build -t boardgames .
docker-compose up --build
echo Now setup the mappings and import the data
echo Now listening on :8080 :5601 and :9200
