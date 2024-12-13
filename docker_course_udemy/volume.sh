docker run -v /home/rahul/docker/django-docker-deployment:/docker_app -v logs:/docker_app/logs  -p 8000:8000 -d --network mynet --name backend backend
docker run --name mongodbb -v /home/rahul/mongo_cont:/data/db -d -p 27017:27017 --network mynet -e MONGO_INITDB_ROOT_USERNAME=rahul -e MONGO_INITDB_ROOT_PASSWORD=rahul111  mongo
