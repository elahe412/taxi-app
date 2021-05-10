import random


def specify_price():
    price_range = range(1000, 100000)
    random_price = random.choice(price_range)
    return random_price
