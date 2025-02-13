FROM python:3.12

RUN DEBIAN_FRONTEND=noninteractive
RUN mkdir /app /work
RUN apt-get update && \
    apt-get install -y chromium chromium-driver vim fonts-ipaexfont-gothic fonts-ipaexfont-mincho && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY main.py /app/
ENTRYPOINT ["/usr/local/bin/python3", "/app/main.py"]
