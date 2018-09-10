# Building Search Driven Apps with Elasticsearch

Elasticsearch is a highly scalable and feature-rich search engine that makes certain types of problems very easy to solve.

This repository contains three (okay, two - the third is handled by [APM](https://www.elastic.co/solutions/apm)) different apps that take advantage of Elasticsearch's capabilities to do really cool things. It's all about using the right tool for the job!

Check out the slides here: [https://github.com/codingblocks/search-driven-apps/blob/master/search-driven-apps.pptx](https://github.com/codingblocks/search-driven-apps/blob/master/search-driven-apps.pptx)

Also, if you're interested in experimenting with Elasticsearch - make sure to check out this [docker-compose file we made that will spin up Elasticsearch, Logstash, and Kibana](https://github.com/codingblocks/simplified-elastic-stack) so you can hit the ground running!

## More about the apps

### Board Games
An ecommerce style website for filtering board games.

```cd boardgames && docker-compose up```

### Podcasts
A simple search powered website that demonstrates fuzzy matching

```cd podcasts && docker-compose up```

### Monitoring
Handled through Kibana

## Troubleshooting
Just run this

```docker kill $(docker ps -q)```

## Notes on deploying with kubernetes
```bash
docker build -f Dockerfile.App -t podcasts-website .
docker tag podcasts-website:latest gcr.io/macro-dolphin-137214/podcasts-website
docker push gcr.io/macro-dolphin-137214/podcasts-website
```

```bash
docker build -f Dockerfile.Logstash -t logstash .
docker tag logstash:latest gcr.io/macro-dolphin-137214/logstash
docker push gcr.io/macro-dolphin-137214/logstash
```

```bash
docker build -f Dockerfile.Apm -t apm .
docker tag apm:latest gcr.io/macro-dolphin-137214/apm
docker push gcr.io/macro-dolphin-137214/apm
```

```bash
cd kubernetes
kubectl create -f namespace-podcasts.json --namespace=podcasts
kubectl config set-context $(kubectl config current-context) --namespace=podcasts
kubectl apply -f . --namespace podcasts
```
