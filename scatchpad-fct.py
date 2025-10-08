### lambda for calculating a triangle area
# area_triangle = lambda base, height: (base*height)/2
# print(area_triangle(2,2))


### partial call of a function
# import functools
# def area_trapezoid(base1, base2, height):
#     return height*(base1 + base2)/2
# area_trapezoid_2 = functools.partial(area_trapezoid, height = 2)
# print(area_trapezoid_2(4,5))


### Crea una función triple que saque el triple de un valor
# import operator
# import functools
# triple = lambda number: operator.mul(number, 3)
# print(triple(3))
# triple2 = functools.partial(operator.mul, 3) # this returns a function
# triple3 = lambda number: triple2(number) # here we call the function
# print(triple3(3))


### Get all combinations of the years 2020-2025 and seasons (range and product)
# import itertools
# years = itertools.count(2020) # returns an iterable with starting at 2020 counting up
## itertools.product creates the cross products of all items in all iterables
## !!!!! A Lot of default iterables are infinite counters/cycles... !!!!!
# combinations = itertools.product(itertools.islice(years, 6), ("spring", "summer", "fall", "winter"))
# print(list(combinations))



# saving a function in a list and doing some stuff to it
# with the range function it doesnt work! -> i is "always" 4
# def create_multipliers():
#     return [lambda x : i * x for i in range(5)]
# # print(create_multipliers())
# for multiplier in create_multipliers():
#     print(multiplier(2))



# Filter: function to filter
# import itertools
# def divisores(n) -> list:
#     return list(itertools.filterfalse(lambda x: n % x != 0, range(2, n)))
# def divisores_primos(n):
#     return list(filter(lambda x: len(divisores(x)) == 0, divisores(n)))
# print(divisores_primos(600851475143))
# # def divisores_primos(n):
# #     solution = []
# #     for divisor in divisores(n):
# #         if len(divisores(divisor)) == 0:
# #             solution.append(divisor)
# #     return solution

# # Hash: never use for crypto!!! We have hashlib for that!
# hashnom = map(hash,['kxe345', 'soyelmejor', 'bananas44'] )
# print(list(zip(hashnom, ['Anastasia', 'Buenaventura', 'Clodovea'])))


# This is returns a generator, wich generates a list of return values, of the size of the parameter
# instead of stopping the function like "return" the function runs on and we collect all "yields" at the end
# def facacum ( n , acum=1) :
#     yield acum*n
#     if n != 1 :
#         yield from facacum( n-1 ,acum*n )
# print(list( facacum ( 4, 2 ) ))
# import random, statistics
# def avg_random(n: int, list: list = []):
#     list.append(random.random())
#     yield statistics.mean(list)
#     if n!= 1:
#         yield from avg_random(n-1, list)
# print(list(avg_random(100)))



# import functools, itertools
# def divisores(n: int) -> list[int]:
#     return list(filter(lambda x: n % x == 0, range(1, n+1)))
# def intersect(a: list[int],b: list[int]):
#     if len(a)>0:
#         if a [len(a) -1] in b:
#             yield a [ len(a) -1]
#         a.pop()
#         yield from intersect(a,b)
# #functools.reduce( lambda a , b : max(list(intersect(divisores(a), divisores(b)))),[3,6,8,4,12,5])
# print(functools.reduce( lambda a , b : a*b // (max(list(intersect(divisores(a), divisores(b))))),[3,6,8,4,12,5]))


# from random import random
# # def mover(positiones: list[int]):
# #     for i, _ in enumerate(positiones):
# #         if random() > 0.3:
# #             positiones[i] += 1
# def mover(positiones: list[int]) -> list[int]:
#     return list(map(rand_increase, positiones))
# rand_increase = lambda x: x+1 if (random() > 0.3) else x
# print(mover([1,1,1,1,1,1,1,1,1,1]))



# import itertools
# def interseccion(a: list, b: list) -> list:
#     return list(filter(lambda x: x in b, a))
# def nointerseccion(a: list, b: list) -> list:
#     return list(itertools.filterfalse(lambda x: x in b, a))
# def union(a: list, b: list):
#     return interseccion(a, b) + nointerseccion(a, b) + nointerseccion(b, a)
# a = [1,2,3]
# b = [3,4,5]
# print(interseccion(a, b))
# print(nointerseccion(a, b), nointerseccion(b, a))
# print(union(a, b))



# import itertools
# def dominada(a: list, b: list):
#     return all(map(lambda x: value_larger_than_all_in_list(x, b),a))
# def dominada2(a: list, b: list):
#     return all(map(lambda x: x[0] > x[1], itertools.product(a, b)))
# def value_larger_than_all_in_list(value: int, list: list):
#     return all(map(lambda x: x < value, list))
# a = [1,2,3]
# b = [4,5]
# c = [3,4]
# print(dominada(b, a), dominada(b, c))
# print(dominada2(b, a), dominada2(b, c))


# import itertools
# def escribe(file,iterable):
#     try:
#         file.writelines(next(iterable))
#     except:
#         file.close()
#         return
#     escribe(file,iterable)
# removed_part1 = itertools.dropwhile(lambda x: x!='***\n', open('lista.txt','r'))
# removed_asterisks = itertools.dropwhile(lambda x: x=='***\n', removed_part1)
# file = itertools.takewhile(lambda x: x!='***\n', removed_asterisks)
# #escribe(open('result','w'),file)
# print(list(file))

