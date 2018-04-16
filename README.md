docker network create elasticnetwork
docker build -t boardgames .
docker run -d -p 8080:80 --name boardgames boardgames -v $(pwd):/var/www "dot net run"
docker run -d --name elasticsearch --net elasticnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.2
docker run -d --name kibana --net elasticnetwork -p 5601:5601 docker.elastic.co/kibana/kibana:6.2.2

docker-compose down
docker build -t boardgames .
docker-compose up --build
echo Now setup the mappings and import the data
echo Now listening on :8080 :5601 and :9200



This image contains the .NET Core SDK, which includes the .NET Core and Command Line Tools (CLI). This image maps to the development scenario. You use this image for local development, debugging, and unit testing. This image can also be used for your build scenarios. Using microsoft/dotnet:sdk always gives you the latest version.
```#```docker-compose -f  .\docker-compose-dev.yml run website  bash```

docker run -p 8080:52914 --name aspnetcore -v .:/app "dot net run"



# For Dev:

```// This will spin up elasticsearch and kibana
docker-compose -f docker-compose-dev.yml up```
```dotnet restore && dotnet build && dotnet run --project .\Website\```

```docker build -t flask-sample:latest .\flask```
```docker-compose -f docker-compose-flask.yml up```



## Questions...

Why does this seem wrong?
If I use docker-compose up and python crashes, I have to restart everything?