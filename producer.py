from kafka import KafkaProducer
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep


def producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda v:
                             json.dumps(v, default=str).encode('utf-8'))

    return producer


def parse_site(producer, url):
    response = urlopen(url)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    text_links = soup.findAll('a', class_='category-page-item-image-text')

    list_of_links = []

    for link in text_links:
        address = link["href"]
        text = link.text
        text = text[1:]
        data = {text: address}
        list_of_links.append(address)
        producer.send('links', value=data)
        # sleep(1)

    print(list_of_links)

    count_of_links = len(list_of_links)

    return list_of_links, count_of_links


def parse_items(producer, list_of_links, number_link):
    url = list_of_links[number_link]
    response = urlopen(url)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll('section', class_='recipe-meta-container two-subcol-content clearfix')

    for link in links:
        text = link.text
        text = text.replace("\n", " ")
        producer.send('meal', value=text)
        # sleep(1)
