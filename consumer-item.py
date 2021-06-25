from kafka import KafkaConsumer
import csv


def consumer_items():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(['meal'])

    for message in consumer:
        print(message)
        write_into_csv(message)


def write_into_csv(message):
    with open('ingredients.csv', mode='a') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(message)


consumer_items()