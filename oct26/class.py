# # Eratosthenes algo

# n = 101 # We want to find primes up to and including 100
# sieve = [True] * n # Initialize the sieve with True values
# sieve[0] = sieve[1] = False # 0 and 1 are not primes
# for i in range(2, int(n**0.5) + 1): # Only go up to the square root of n
#     if sieve[i]: # If i is a prime
#  # Set all multiples of i to False
#         for j in range(i*i, n, i): # Start from i*i, as smaller multiples would have already been marked
#             sieve[j] = False

        
# # Done! Now print the list of primes.
# for i in range(n):
#  if sieve[i]:
#     print

# monte carlo method 
from math import sqrt
from random import random
count=0
for i in range(1000000): # for a large sample
    x=random()
    y=random()

    if sqrt(x*x+y*y)<1:
        count+=1

print(4*(count/1000000)) # pi estimation