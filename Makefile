# Get the current user ID and group ID, to run the Docker containers as (host current) unprivileged user, instead of root.
UID := $(shell id -u)
GID := $(shell id -g)

DOCKER_COMPOSE_RUN = docker compose run --rm --user $(UID):$(GID) bot

up:
	docker compose up

install:
	$(DOCKER_COMPOSE_RUN) /bin/sh -c "python -m venv venv && . venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

init-db:
	$(DOCKER_COMPOSE_RUN) /bin/sh -c ". venv/bin/activate && python src/init_db.py"

run:
	$(DOCKER_COMPOSE_RUN) /bin/sh -c ". venv/bin/activate && python src/bot.py"

test:
	$(DOCKER_COMPOSE_RUN) /bin/sh -c ". venv/bin/activate && pytest"

down:
	docker compose down

clean:
	rm -rf data/*.db logs/*.log __pycache__ .pytest_cache venv
