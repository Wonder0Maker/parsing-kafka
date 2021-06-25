from kafka import KafkaConsumer


def consumer_parse():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(['links'])

    for message in consumer:
        print(message)


consumer_parse()