import random, statistics
def avg_random(n: int, list: list = []):
    list.append(random.random())
    yield statistics.mean(list)
    if n!= 1:
        yield from avg_random(n-1, list)
print(list(avg_random(100)))