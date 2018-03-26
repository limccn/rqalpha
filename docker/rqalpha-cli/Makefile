IMG:=`cat Name`
GRANT_USER:=rqalpha
MOUNT:=-v `pwd`/work:/root/work
DOT_ENV:=--env .env
USER_SET:=--user rqalpha
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
                       $(DOT_ENV) $(MOUNT) $(IMG) 

run_i:
	docker rm $(CONTAINER_NAME) || echo
	docker run -it --name $(CONTAINER_NAME) $(LINK_MAP) $(PORT_MAP) \
                       $(DOT_ENV) $(USER_SET) $(MOUNT) $(IMG) start.sh ~/work/run_stragegy.sh

stop:
	docker stop $(CONTAINER_NAME);


rm:	stop
	docker rm $(CONTAINER_NAME)

