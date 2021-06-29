from kafka import KafkaConsumer
import csv
import pandas as pd


def consumer_items():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    consumer.subscribe(['meal'])

    for message in consumer:
        print(message)

        ingredients = pd.DataFrame([message.value.decode('utf-8')], columns=['Ingredient'])
        ingredients.to_csv('ingredients.csv', index=False, mode='a', header=False)


consumer_items()