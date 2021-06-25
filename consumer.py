from kafka import KafkaConsumer


def consumer_parse():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(['mt2'])

    for message in consumer:
        print(message)


def consumer_items():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(['meal'])

    for message in consumer:
        print(message)
