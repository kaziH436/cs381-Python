# Generate and print all prime numbers 1 and 100
import math
for n in range(1, 101):
    if n < 2:
        continue
    if n % 2 == 0 and n != 2:
        continue

    is_prime = True
    k = 3
    while k * k <= n:
        if n % k == 0:
            is_prime = False
            break
        k += 2              # only odd divisors, since evens are already ruled out
    if is_prime:
        print(n)


for i in range(1, 10):
    print((i - 1) * ' ', end='')   # leading spaces
    for j in range(i, 10):         # count up: i to 9
        print(j, end='')
    for j in range(8, i - 1, -1):  # count back down: 8 to i
        print(j, end='')
    print()




# # both break and continue takes back to the top of the loop
# for i in range(1,5):
#     for j in range(1,5):
#         if (i+j)%2==0:
#             break 
#         print(f'({i},{j})', end='')
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print(f'({i},{j})', end="") 
#     print()


# lamda expression, short form fora fucntionn 
 
a=lambda 

a=lambda x, y=x+y