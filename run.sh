docker build -t boardgames .
docker run -d -p 8080:80 --name boardgames boardgames
