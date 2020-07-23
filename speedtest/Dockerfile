FROM python:3.6-alpine

# RUN apt-get update && apt-get install -y python-pip

RUN mkdir /app
RUN pip install speedtest-cli
RUN pip install prometheus-client

COPY run-speedtest.py /app/
WORKDIR /app
EXPOSE 9104
ENTRYPOINT ["python", "run-speedtest.py"]
