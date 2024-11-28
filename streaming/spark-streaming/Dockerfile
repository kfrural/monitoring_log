FROM openjdk:11

RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY kafka_spark_stream.py /app/kafka_spark_stream.py
WORKDIR /app

CMD ["python3", "kafka_spark_stream.py"]
