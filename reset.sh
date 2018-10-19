echo "Stopping docker containers"
docker stop $(docker ps -aq)

echo "Removing docker containers"
docker rm $(docker ps -aq)

echo "Opening sites, these will need to be refreshed after the containers come up" 
open http://localhost:5000/
open http://localhost:5001/
open http://localhost:5601/

echo "Starting up containers"
docker-compose up
