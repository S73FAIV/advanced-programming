####################################################
# Largest Prime Factor
#
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
######################################################

# we solved that in advanced programming

import itertools

def divisores(n) -> list:
    return list(itertools.filterfalse(lambda x: n % x != 0, range(2, n)))

def divisores_primos(n):
    return list(itertools.filterfalse(lambda x: len(divisores(x)) != 0, divisores(n)))

print(divisores_primos(600851475143))
