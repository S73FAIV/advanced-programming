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


# import numpy as np
# from pprint import pprint

# matrix = np.linspace(-100, 100, 10).reshape(2, 5)
# pprint(matrix)
# pprint(matrix.shape)
# vector = np.linspace(-5,5,5).reshape(5,1)
# pprint(vector.shape)
# pprint(vector)

# pprint(matrix @ vector)
# #pprint(matrix.mean(axis=0))

# a = np.linspace(-10, 10, 8).reshape(4,2)
# pprint(a)
# pprint(a.reshape(2,2,2))



# ###
# import math, numpy
# # y=[]
# # t=0
# # while t<=10:
# #     y.append(math.sin(t))
# #     t+=0.01
# y = map(lambda x: math.sin(x), numpy.linspace(0,10,1000))
# print(list(y))
# # better:
# t = numpy.arange(0, 10.01, 0.01)
# y = numpy.sin(t)


# import numpy
# # D = [0.2, 1.0 ,1.5, 3.0, 1.0, 4.2, 3.14]
# # if all([x<10 for x in D]):
# #     print('Todos pequeños')
# a = numpy.array([0.2, 1.0 ,1.5, 3.0, 1.0, 4.2, 3.14])
# b = a < 10
# #print(b)
# if numpy.all(b): print('Todos pequeños')


# import numpy
# x = numpy.array([2, 1, 2, 2, 3, 1 ,3, 2 , 1 ,3])
# y = x == 2
# cuenta = numpy.count_nonzero(y)
# print(cuenta)



# import numpy
# time = numpy.linspace(20, 145, 5)
# sers = numpy.sin(numpy.arange(20)).reshape(5,4)

# print(time, sers)
# print(numpy.max(sers, axis=1))
# positions = numpy.argmax(sers, axis=1)
# print(positions)
# print(time.take(positions))


# #a+b*c for all combinations of elements (Cartesian product)
# import numpy as np
# a=np.array([2,3,4,5])
# b=np.array([8,5,4])
# c=np.array([5,4,6,8,3])
# # for i in a:
# #     for j in b:
# #         for k in c:
# #             print(i, "+", j, "*", k, "=", i+j*k)
# Ai, Bj, Ck = np.ix_(a, b, c)
# result = Ai + Bj * Ck  
# print(result)


# In the ‘intensity’ file, we have a record of the wireless connection signal strength
# on a series of devices that are being monitored minute by minute. Each
# line shows the signal strength on each device on a scale of 0 to 5
# We are interested in the time that a device is continuously without a signal, that is, we
# look at how long it takes to recover the signal. Create a programme that asks on the
# screen how many devices there are and writes which device has suffered the
# longest continuous time without a signal, that is, locate the longest time without a signal and say on
# which device it was.
# You must use a function other than main, dividing the work into similar parts and
# passing arguments.
# import numpy
# values = []
# with open("intensity.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         values.append(line.split())
# values = numpy.array(values, dtype=int)
# num_maschines = values.shape[1]
# longest_outage = 0
# failed_maschine = -1
# for maschine in range(values.shape[1]):
#     current_outage = 0
#     for minute in range(values.shape[0]):
#         if values[minute][maschine] == 0:
#             current_outage += 1
#         else: 
#             current_outage = 0
#         if current_outage > longest_outage:
#             longest_outage = current_outage
#             failed_maschine = maschine
# print(failed_maschine)
# print(longest_outage)


# import pandas
# data = pandas.read_csv("intensity.txt", sep=" ")
# data.columns=["m1", "m2", "m3"]
# #data = pandas.DataFrame(data=["1", "2", "3", "4", "3"], columns=["Name"])
# # print(data.groupby(data["Name"]).groups)
# # count = map(lambda x: data., data["Name"].unique())
# print(data.describe()["m3"], data.shape)


# Prepare a CSV file or spreadsheet with columns for the
# names, heights, and weights of several people. Upload it and
# calculate the average height of those above and below a
# given value.
# Also write down how many there are of each type.
# import pandas
# THRESHOLD_HEIGHT=135
# data = pandas.read_csv("exercise-persons.csv")
# print(data[data["height"] < THRESHOLD_HEIGHT].height.mean(), 
#       data[data["height"] < THRESHOLD_HEIGHT].height.count())
# print(data[data["height"] > THRESHOLD_HEIGHT].height.mean(),
#       data[data["height"] > THRESHOLD_HEIGHT].height.count())
# print(data.shape)


# We have a list of numbers
#Example:
# price = [3.67, 4.3, 8.9, 5.1]
# tax = [10, 21, 5, 21]
# imputations = []
# for p, t in zip(price, tax):
#     imputations.append(p*t/100)
# print(imputations)

# import pandas
# pprice = pandas.Series(price)
# ptax = pandas.Series(tax)
# print(pprice*ptax/100)


# import functools
# def area_trapecoid(base: int, top: int, height: int):
#     return height*(base+top)/2
# area_trapecoid_height_2 = functools.partial(area_trapecoid, height=2)
# print(area_trapecoid_height_2(4,5))


# import operator
# def triple(number: int):
#     return operator.mul(number, 3)


# import itertools
# c=itertools.count(2020)
# e=itertools.cycle(('prim','ver','oto','inv'))
# f=itertools.islice(zip(c,e),1,6,2)
# print(list(f))
# import itertools
# print(list(itertools.product(range(2020, 2026), ("spring", "summer", "fall", "winter"))))


# import operator
# mymap = map(lambda x: x*x, range(10,21))
# print(list(mymap))
# print(list(mymap))


# import itertools
# def divisores(n: int) -> list[int]:
#     return list(itertools.filterfalse(lambda x: n%x!=0,range(2,n)))
# def is_prime(n: int) -> bool:
#     return len(divisores(n)) == 0
# def prime_divisors(n: int) -> list[int]:
#     return list(filter(is_prime, divisores(n)))
# A = 24
# print(divisores(A))
# print(is_prime(A))
# print(prime_divisors(A))


# nombres = ['Anastasia','Buenaventura', 'Clodovea']
# passwords = map(hash, ['kxe345','soyelmejor','bananas44'])
# print(list(zip(nombres,passwords)))
#Crear una lista (nombre,hash(clave))


## Yield as special Generator-Syntax
# def facacum ( n , acum=1) :
#     yield acum*n
#     if n!= 1 :
#         yield from facacum( n-1 ,acum*n )
# print(list( facacum(6) ))
# import random, statistics
# def alea_avg(number: int, counter: int = 0):
#     alea_list = []
#     for i in range(counter+1):
#         alea_list.append(random.random())
#     yield statistics.mean(alea_list)
#     if counter <= number:
#         yield from alea_avg(number, counter+1)

# print(list(alea_avg(100)))
# import random, statistics
# def avg_random(n: int, list: list = []):
#     list.append(random.random())
#     yield statistics.mean(list)
#     if n!= 1:
#         yield from avg_random(n-1, list)
# print(list(avg_random(100)))


import itertools
def divisores(n: int) -> list[int]:
    return list(itertools.filterfalse(lambda x: n%x!=0,range(2,n)))
def is_prime(n: int) -> bool:
    return len(divisores(n)) == 0
def prime_divisors(n: int) -> list[int]:
    return list(filter(is_prime, divisores(n)))
# A = 24
# print(divisores(A))
# print(is_prime(A))
# print(prime_divisors(A))
import functools
def intersection(a, b):
    if len(a) > 0:
        if a[len(a)-1] in b:
            yield a[len(a)-1]
        a.pop()
        yield from intersection(a, b)

print(
    functools.reduce(
    lambda a, b: max(
        list(
            intersection(divisores(a), divisores(b))
            ),
        default=1
        ), 
    [3, 6, 8, 4, 12, 5]
))


