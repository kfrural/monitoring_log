import time
import pytest
from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "test_topic"


@pytest.fixture(scope="module")
def producer():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
    yield producer
    producer.close()


@pytest.fixture(scope="module")
def consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest", 
        group_id="test-group",
    )
    yield consumer
    consumer.close()


def test_kafka_producer_and_consumer(producer, consumer):

    test_message = "Test Kafka Message"

    producer.send(KAFKA_TOPIC, value=test_message.encode("utf-8"))
    producer.flush()

    time.sleep(1)

    consumer.poll()
    messages = consumer.messages()

    assert any(test_message.encode("utf-8") in message.value for message in messages)
