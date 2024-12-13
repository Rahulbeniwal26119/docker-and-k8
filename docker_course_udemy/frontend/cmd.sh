docker run -d --name backend  -p 8000:8000 --network mynet backend
docker run -d --name mongodb  -p 27017:27017 --network mynet mongo
docker run -d --name frontend -p 3000:3000 --network mynet frontend
