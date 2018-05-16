# Building Search Driven Apps with Elasticsearch

Elasticsearch is a highly scalable and feature-rich search engine that makes certain types of problems very easy to solve.

This repository contains three (okay, two - but the third is comign soon!) different apps that take advantage of Elasticsearch's capabilities to do really cool things. It's all about using the right tool for the job!

## Board Games
An ecommerce style website for filtering board games.

```cd boardgames && docker-compose up```

## Podcasts
A simple search powered website that demonstrates fuzzy matching

```cd podcasts && docker-compose up```

## Monitoring
A simple monitoring website that demonstrates application performance management

```cd monitoring && docker-compose up```

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
cd kubernetes
kubectl create -f namespace-podcasts.json --namespace=podcasts
kubectl config set-context $(kubectl config current-context) --namespace=podcasts
kubectl apply -f . --namespace podcasts
```