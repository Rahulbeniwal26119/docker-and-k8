## Deployment (K8)

### Start Minikube
    minikube start --driver=docker

### Build Image for project
    docker build .

### Tag image with Docker Hub image name (if not tagged on build state)
    docker tag backend  {{uname}}/{{image_name}}

### Push Image to Docker Hub
    docker push {{uname}}/{{image_name}}

### Create a deployment for above image
    kubectl create deployment backend --image={{uname}}/{{image_name}}

### Delete a deployment
    kubectl delete deployment backend

### Run K8 Dashboard
    minikube dashboard

#
#
#

## Service
Till  now pods are running but not reachable from external environment let's use service for this

Expose types
1. CusterIP -> Will only be reachable from inside the cluster but ip would not be changed
2. NodePort -> deployment should be exposed with ip address of worker node
3. LoadBalancer -> Utitlize load balance and load balance will generate address for service.

### Exposing port
    kubectl expose deployment backend --type=LoadBalancer --port 8000

### Get service status
    kubectl get services

### Minicube specific command to provide external ip to deployment (localhost only)
    minikube service backend