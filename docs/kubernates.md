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

### Delete service
    kubectl delete service backen

### Minicube specific command to provide external ip to deployment (localhost only)
    minikube service backend

## scaling pods
    kubectl scale deployment/backend --replicas=3

## Restrarting a deployment
    kubectl rollout restart deployment <deployment_name>


## Get update or restart status
    kubectl rollout status deployment/backend


## Update image
    kubectl set image deployment/<deployment_name>  <container_name>=<image_source_docker_hub>:<image_tag>

    Eg: kubectl set image deployment/backend  kube-backend=rbeniwal26119/kube-backend:2

## Roollout Failed pods or deployments

    kubectl rollout undo deployment/backend

## Get Rollout history
     kubectl rollout history deployment/backend
    
## Rollout to revision
    kubectl rollout undo deployment/backend --to-revision=1

## Create a master deployment file with all kube objects
    combine all specification file and seprate them with --- (Order Matters)

## Update deployment from specification files
    kubectl apply -f=kube-volumes.yaml

## Assigning a group to related kube objects
    Update metadata section as
    
    metadata:
      labels:
        group: group_name

## Stopping all kube object (deployment, services and others) by group
    kubectl delete deployments,service -l group=group_name
