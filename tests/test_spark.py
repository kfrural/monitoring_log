import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from kafka import KafkaProducer
import time

@pytest.fixture(scope="module")
def spark():
    spark_session = SparkSession.builder \
        .appName("SparkKafkaTest") \
        .getOrCreate()
    yield spark_session
    spark_session.stop()

@pytest.fixture(scope="module")
def kafka_producer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    yield producer
    producer.close()

def test_spark_streaming_with_kafka(spark, kafka_producer):

    topic = "test-topic"
    test_message = '{"key": "value"}'
    kafka_producer.send(topic, value=test_message.encode('utf-8'))
    kafka_producer.flush()

    kafka_stream_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", topic) \
        .load()

    message_df = kafka_stream_df.selectExpr("CAST(value AS STRING)").alias("message")

    query = message_df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    time.sleep(5)

    query.stop()

    assert query.isActive is False

