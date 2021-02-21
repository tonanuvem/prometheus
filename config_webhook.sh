echo "Digite a URL que está no canal #webhook do SLACK:"
read WEBHOOK

sed -i 's|inserir_webhook|'$WEBHOOK'|' alertmanager/config.yml
# sed -i 's|lab-monitoracao|lab-testes|' alertmanager/config.yml
