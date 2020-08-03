[[ -n "$(docker ps -qa)" ]] && docker rm -f $(docker ps -qa)
[[ -n "$(docker volume ls -q)" ]] && docker volume rm -f $(docker volume ls -q)
docker network rm  $(docker network ls -q)
