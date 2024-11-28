from kafka import KafkaConsumer

consumer = KafkaConsumer('server-logs', bootstrap_servers='localhost:9092')
for message in consumer:
    print(f"Mensagem recebida: {message.value.decode()}")
