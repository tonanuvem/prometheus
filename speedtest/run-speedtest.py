#!/usr/bin/python

import speedtest
import time
from prometheus_client import start_http_server, Summary, Gauge

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
  s.download()
  s.upload()
  results_dict = s.results.dict()
  g_download.set(results_dict["download"])
  g_upload.set(results_dict["upload"])
  print("upload: %s" % (results_dict["upload"]))
  print("download: %s" % (results_dict["download"]))
  time.sleep(t)
  
if __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(9104) 
  # Generate some requests.
  while True:
    try:
      process_request(test_interval)
    except TypeError:
      print("TypeError returned from speedtest server")
    except socket.timeout:
      print("socket.timeout returned from speedtest server")
