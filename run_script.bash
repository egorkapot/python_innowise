#!/usr/bin/env bash

# Stop the script if any commands fail

# Check if Docker is already installed
if command -v docker > /dev/null && command -v docker-compose &> /dev/null; then
    echo "Docker environment is already installed"
else
    # Install dependencies and add the Docker repository
    apt-get update -y
    apt-get install ca-certificates curl gnupg lsb-release -y
    mkdir -p /etc/apt/keyrings
    curl -fsSL -q https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

    # Install Docker and Docker Compose
    apt-get install docker-ce docker-ce-cli containerd.io -y
    curl -L -q "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    echo "Docker has been installed"
fi

docker stop $(docker ps)
docker rm $(docker ps -a)
docker rmi egor_test

# Build the Docker image
docker build -t egor_test .

# Set the name of the Docker Compose file
COMPOSE_FILE=docker-compose.yml

# Run the Docker Compose file
docker-compose -f $COMPOSE_FILE up -d

# Print the logs for all containers
# docker-compose -f $COMPOSE_FILE logs



