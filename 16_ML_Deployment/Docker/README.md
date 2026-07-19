# Containerizing ML Services with Docker

Docker packages code, dependencies, and environment configurations into a single container image. This guarantees that your model api runs identically in testing, staging, and production environments, eliminating "it works on my machine" issues.

---

## Essential Docker Command Roadmap

### 1. Building the Image
Builds a Docker image from the local `Dockerfile` in the current folder, tagging it as `student-api:v1`:
```bash
docker build -t student-api:v1 .
```

### 2. Listing Images
Shows all local Docker images stored on your machine:
```bash
docker images
```

### 3. Running the Container
Runs the image inside an isolated container, mapping port 8000 of your local machine to port 8000 of the container:
* `-d`: Run in background (detached mode).
* `-p`: Bind local_port:container_port.
```bash
docker run -d -p 8000:8000 --name student-service student-api:v1
```

### 4. Checking Running Containers
Lists all active running containers:
```bash
docker ps
```
Use `docker ps -a` to view all containers (including stopped or crashed ones).

### 5. Viewing Container Logs
Inspects the standard console output/logs of a running container:
```bash
docker logs student-service
```

### 6. Executing Commands Inside the Container
Opens an interactive bash terminal inside a running container:
```bash
docker exec -it student-service bash
```

### 7. Stopping and Removing Containers
```bash
# Stop the active container
docker stop student-service

# Delete the stopped container
docker rm student-service

# Delete the built image
docker rmi student-api:v1
```
