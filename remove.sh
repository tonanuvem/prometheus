#!/bin/bash

docker compose stop && docker compose rm -f && docker volume prune -f && git pull
echo ""
echo "Removendo volumes:"
echo ""
# Lista todos os volumes e remove cada um
docker volume ls -q | grep prometheus | while read volume; do
  #echo "Removendo volume: $volume"
  docker volume rm "$volume"
done
