IMAGE_TAG = $(tag)
DOCKERFILE = $(df)
COMPOSEFILE = $(cf)
ENVFILE = $(env)

docker-build: 
	@docker build -t $(IMAGE_TAG) -f $(DOCKERFILE) --no-cache .

docker-up:
	@docker compose -f $(COMPOSEFILE) --env-file .env up -d

docker-down:
	@docker compose -f $(COMPOSEFILE) --env-file .env down --remove-orphans

docker-buildup: \
	docker_build \
	docker_up
