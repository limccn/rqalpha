IMG:=`cat Name`
GRANT_USER:=jovyan
MOUNT:=-v `pwd`/work:/home/$(GRANT_USER)/work
DOT_ENV:=--env .env
USER_SET:=--user root
NOTEBOOK_TOKEN:=''
FW_PORT:=8888
EXPOSE_PORT:=8888
PORT_MAP:=-p $(FW_PORT):$(EXPOSE_PORT)
#LINK_MAP:=--link xxx:xxx
CONTAINER_NAME:=docker-rqalpha

echo:
	echo $(IMG)

build:
	docker build -t $(IMG) ./

run:
	docker rm $(CONTAINER_NAME) || echo
	docker run -d --name $(CONTAINER_NAME) $(LINK_MAP) $(PORT_MAP) \
                       $(DOT_ENV) $(MOUNT) $(IMG) start-notebook.sh \
 --NotebookApp.token=$(NOTEBOOK_TOKEN)


run_i:
	docker rm $(CONTAINER_NAME) || echo
	docker run -it --name $(CONTAINER_NAME) $(LINK_MAP) $(PORT_MAP) \
                       $(DOT_ENV) $(USER_SET) $(MOUNT) $(IMG)  /bin/bash

stop:
	docker stop $(CONTAINER_NAME);


rm:	stop
	docker rm $(CONTAINER_NAME)

