FROM ubuntu:14.04

RUN apt-get update && apt-get install -y wget && apt-get clean
RUN apt-get update && apt-get install -y python
RUN apt-get update && apt-get install -y default-jdk

RUN wget https://archive.apache.org/dist/spark/spark-1.5.2/spark-1.5.2-bin-hadoop2.6.tgz && \
    tar -xzf spark-1.5.2-bin-hadoop2.6.tgz && \
    mv spark-1.5.2-bin-hadoop2.6 /spark && \
    rm spark-1.5.2-bin-hadoop2.6.tgz

RUN apt-get update && apt-get install -y python3-pip

COPY /main.py /app/main.py

CMD ["/spark/bin/spark-submit", "--master", "local[*]", "/app/main.py"]
