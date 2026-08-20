#!/bin/bash

docker compose stop && docker compose rm -f && docker volume prune -f && git pull
echo ""
echo "Removendo volumes:"
echo ""
# Lista todos os volumes e imagens e remove cada um
docker compose down --volumes
docker image prune -f
