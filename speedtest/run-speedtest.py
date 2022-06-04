#!/usr/bin/python

import speedtest
import time
from prometheus_client import start_http_server, Summary, Gauge
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

servers = []
# If you want to test against a specific server
# servers = [1234]

test_interval = 60 # initiate speed test every 60 seconds

s = speedtest.Speedtest()

g_download = Gauge('download_speed', 'Download speed')
g_upload = Gauge('upload_speed', 'Upload speed')

def process_request(t):
  s.get_servers(servers)
  s.get_best_server()
  logging.warning("Aplicacao Speed Test selecionou SERVIDORES para efetuar os testes de velocidade")
  s.download()
  logging.warning("Aplicacao Speed Test fez testes de velocidade de DOWNLOAD")
  s.upload()
  logging.warning("Aplicacao Speed Test fez testes de velocidade de UPLOAD")
  results_dict = s.results.dict()
  g_download.set(results_dict["download"])
  g_upload.set(results_dict["upload"])
  print("\tupload: %s" % (results_dict["upload"]))
  print("\tdownload: %s" % (results_dict["download"]))
  time.sleep(t)
  
if __name__ == '__main__':
  # Start up the server to expose the metrics.
  logging.warning("Aplicacao Speed Test foi iniciada")
  start_http_server(9104) 
  # Generate some requests.
  while True:
    try:
      process_request(test_interval)
      logging.warning("Speed Test logou as velocidades")
    except TypeError:
      print("TypeError returned from speedtest server")
      logging.error("Speed Test except TypeError")
    except socket.timeout:
      print("socket.timeout returned from speedtest server")
      logging.error("Speed Test except socket.timeout")
