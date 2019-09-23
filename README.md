# visits-flask

ssh vm #1
- init swarm
> docker swarm init

ssh vm #2 
- add this worker (vm2) to swarm (vm1) :
> docker swarm join --token <TOKEN> <IP:PORT>

vm #1
- on  manager, deploy application :
> docker stack deploy -c docker-compose.yml flask-swarm

- check :
> docker stack ps flask-swarm
