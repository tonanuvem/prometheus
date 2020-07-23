FROM python3:alpine

# RUN apt-get update && apt-get install -y python-pip

RUN mkdir /app
RUN pip install speedtest-cli
RUN pip install prometheus-client

COPY run-speedtest.py /app/

EXPOSE 9104
ENTRYPOINT ["/usr/bin/python", "-u", "/app/run-speedtest.py"]
