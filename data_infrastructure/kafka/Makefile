PYTHON = python3
VENV = .venv
VENV_BIN = $(VENV)/bin
PYTHON_VENV= $(VENV_BIN)/python3

DOCKER_COMPOSE = ./docker-compose.yml


# setup_python_env:
# 	@echo "Create Python venv environment"
# 	@$(PYTHON) -m venv $(VENV)
# 	@$(VENV_BIN)/pip install -U pip
# 	@$(VENV_BIN)/pip install -r requirements.txt
# 	@echo "Complete"

setup_docker: 
	@docker compose -f $(DOCKER_COMPOSE) build 
	@docker compose -f $(DOCKER_COMPOSE) up  -d

setup_infras: setup_docker

# setup: setup_python_env setup_infras

docker_up:
	@docker compose -f $(DOCKER_COMPOSE) up  -d

docker_down:
	@docker compose -f $(DOCKER_COMPOSE) down

docker_remove: 
	@docker compose -f $(DOCKER_COMPOSE) down -v --rmi all
