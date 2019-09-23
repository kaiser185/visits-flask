# visits-flask

Using Google Cloud Platform (GCP)

# Prerequites :
- GCP
- Docker
- Docker Swarm

- Create 2 VM :
> docker-machine create --driver google \
	--google-project skilled-index-253808 \
	--google-machine-type g1-small \
	--google-open-port 80 \
	--google-open-port 8080 vm1

> docker-machine create --driver google \
	--google-project skilled-index-253808 \
	--google-machine-type g1-small \
	--google-open-port 80 \
	--google-open-port 8080 vm2 

- connect to vm #1 :
> docker-machine ssh vm1

- init swarm
> docker swarm init

- ssh vm #2 
- add this worker (vm2) to swarm (vm1) :
> docker swarm join --token TOKEN <IP:PORT>
Replace TOKEN, adress IP and PORT

vm #1
- on  manager, deploy application :
> docker stack deploy -c docker-compose.yml flask-swarm

- check :
> docker stack ps flask-swarm

- see web site :
``` 
IP:80 
```

- see visualizer :
``` 
IP:8080 
```

