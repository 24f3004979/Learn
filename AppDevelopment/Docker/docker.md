# Docker Flow
A tool to manage our application, managing its dependencies and requirements into a isolated way for easy deployment.

**Architechture**
Client server architechture, with docker client and daemon working for making the environment possible for application.

client and daemons are independent of each others, thus we can have our client into application talking to daemon at remote with network interface or unix sockets.

### Docker daemon | dockerd 
Listens to  docker api request and manages objects as images, containers, network and volumes. Multiple daemon can communicate for a service.

### Images
read-only templates, instructions to create a Docker container, we may make our own image with customization.

we can create a docker file with syntax for defining steps for creating image tok run it, Each instruction creates a layer in docker file creates a layer in the image.

Upon changing the docker file and re-build the only changed part is rebuild,

### Containers
Runnable instances of images, create, start, stop, move or delete using docker api or cli, 
