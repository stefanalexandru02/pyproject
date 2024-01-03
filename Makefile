PROJECT_NAME=aerostar
PROJECT_CONTAINER_NAME_PREFIX=aerostar

export COMPOSE_FILE=compose.yml

.PHONY: up down stop prune ps shell logs tests

default: up

help : Makefile
	@sed -n 's/^##//p' $<

up:
	@echo "Starting up containers for for $(PROJECT_NAME) using $(COMPOSE_FILE)..."
	docker-compose up --build -d --remove-orphans

build:
	@echo "Building with no cache python image for for $(PROJECT_NAME)..."
	docker-compose build --no-cache

down: stop

start:
	@echo "Starting containers for $(PROJECT_NAME) from where you left off..."
	@docker-compose start

stop:
	@echo "Stopping containers for $(PROJECT_NAME)..."
	@docker-compose stop

prune:
	@echo "Removing containers for $(PROJECT_NAME)..."
	@docker-compose down -v $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
