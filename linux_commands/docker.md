# Stop all containers
`docker stop $(docker ps -a -q)`

# Remove all containers
`docker rm $(docker ps -a -q)`

# Remove all stopped containers
`docker container prune`

# Clean system
`docker system prune`

# Remove all dangling volumes (nothing attached?)
`docker volume rm $(docker volume ls -qf dangling=true)`
