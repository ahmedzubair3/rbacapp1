.PHONY: up down build restart ansible-shell run

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

restart: down up

shell:
	docker exec -it ansible bash

setup:
	docker exec -it ansible bash -c "ansible-playbook setup_services.yml -i /inventory/hosts.ini"

action_exists:
ifndef ACTION
	$(error ACTION is not defined. Please set ACTION variable to the desired action.)
endif

action: action_exists
	docker exec -it ansible ansible-playbook actions.yml -i /inventory/hosts.ini -e "action=$(ACTION)"