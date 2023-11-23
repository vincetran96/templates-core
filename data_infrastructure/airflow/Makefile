COMPOSEFILE = $(cf)
DOCKERFILE = $(df)
IMAGE_TAG = $(tag)

docker_build: 
	@docker build -t $(IMAGE_TAG) -f $(DOCKERFILE) --no-cache .

docker_up:
	@docker compose -f $(COMPOSEFILE) up -d

docker_down:
	@docker compose -f $(COMPOSEFILE) down

docker_buildup: docker_build docker_up
