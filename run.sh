#!/bin/sh

# Liberando a porta no caso de rodar no Cloud9
sudo service mysql stop

docker compose up -d

echo ""
echo "Aguardando a configuração..."

# espera o airflow subir
while ! docker logs grafana 2>&1 | grep -q "HTTP Server Listen"; do
  printf "."
  sleep 2
done
echo " ✅"

echo ""
echo "Projeto iniciado!"

# pega IP público
IP=$(curl -s checkip.amazonaws.com)

echo ""
echo "========================================"
echo "        AMBIENTE PRONTO 🚀"
echo "========================================"
echo ""
echo "🚀 Speedtest:"   && echo "   URL : http://$IP:9104"
echo ""
echo "🔥 Prometheus:"  && echo "   URL : http://$IP:9090"
echo ""
echo "📊 Grafana:"     && echo "   URL : http://$IP:3000"
echo ""
echo "========================================"
echo ""
