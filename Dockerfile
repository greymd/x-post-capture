FROM python:3.12

RUN DEBIAN_FRONTEND=noninteractive
RUN mkdir /app
RUN apt-get update && \
    apt-get install -y chromium chromium-driver vim fonts-ipaexfont-gothic fonts-ipaexfont-mincho && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY main.py .
ENTRYPOINT ["/usr/local/bin/python3", "main.py"]
