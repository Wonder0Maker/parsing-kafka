from producer import producer, parse_site, parse_items

if __name__ == '__main__':

    url = "https://www.allrecipes.com/recipes/859/desserts/cookies/sugar-cookies/"

    producer = producer()
    items, count_of_items = parse_site(producer, url)

    for i in range(0, count_of_items):
        parse_items(producer, items, i)
