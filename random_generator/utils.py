from random import randint


def generate_random(x=0, y=0):
    try:
        print(0)
    except RecursionError as re:
        pass
    x = randint(x, x + 5)
    y = randint(x, x + 5)
    generate_random(x, y)
