from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('server-logs', b'Teste de mensagem no Kafka')
producer.flush()
