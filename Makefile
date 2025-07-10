# Makefile for managing the rbcapp_monitoring project

PROJECT_NAME = rbcapp1
DOCKER_COMPOSE = docker-compose

.PHONY: build up down shell logs restart

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

shell:
	docker exec -it $(PROJECT_NAME) /bin/bash

run_task3:
	docker exec -it $(PROJECT_NAME) bash -c "cd /app;  ./task3_runner.sh"

logs:
	docker logs -f $(PROJECT_NAME)

restart:
	$(DOCKER_COMPOSE) restart $(PROJECT_NAME)
