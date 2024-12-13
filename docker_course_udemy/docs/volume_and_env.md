## Command to create a names volume with django

    docker run -p 8000:8000 -v logged_users:/docker_app/logged_details 1265ee914834

### Command for creating a mounted volume

    docker run --network=host -v "/home/rahul/docker/docker_mount":"/docker_app/logged_details" django_docker:latest

### How to run docker container as develpment server
    docker run  --network=host --name=docker_app -v "/home/rahul/docker/django-docker-deployment:/docker_app" django_docker
    
1) Mount the running docker container to the same location the project location

2) files in mount has preferance over container code   

### command for making some file system under mounted source as read only
    docker run --network=host -v "/home/rahul/docker/django-docker-deployment:/docker_app:ro" -v docker_app/logs   django_docker:latest 

1) Keep container under the container constant except the logs file

### inspecting the volume path in local storage
docker volume inspect 1a2fd0f9e679337e4c856f71fd317a723518f2cbd914ca902f16a62c2a5fafcd

1) MountPoint shows the path where volume mounter on local
 
### Adding Environment Variable 
#### Env are active on container run
<li>keeping adding -e if there are multiple</li>
<div style="margin-left:30px">
    <code>docker run -p 8000:80 --env PORT=80  django_docker</code>
</div>
<div style="margin-left:30px">
    <code>docker run -p 8000:80 -e PORT=80  django_docker</code>
</div>

<li>reading from a file</li>
<div style="margin-left:30px"><code>docker run -p 8000:80 --env-file .env django_docker</code></div>


### Build Args
<li>Build args are passed when building the image these are mainly use to replace docker images variables by values given when building image</li> 
<br>
<p style="margin-left:30px" > Defined as </p>
<div style="margin-left:30px"> <i> <b>ARG DEFAULT_PORT=8000</i> <br> <i>ENV PORT ${DEFAULT_PORT}</b></i>
</div>
<br>
<div style="margin-left:30px">
    <code>docker build -t django_docker:dev --build-arg DEFAULT_PORT=9000 . </code>
</div>