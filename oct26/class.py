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
# from math import sqrt
# from random import random
# count=0
# for i in range(1000000): # for a large sample
#     x=random()
#     y=random()

#     if sqrt(x*x+y*y)<1:
#         count+=1

# print(4*(count/1000000)) # pi estimation


# d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(d[1:len(d):2])
# def delete_at_even_positions(x):
#     del x[1:len(x):2]

# delete_at_even_positions(d)
# print(d)

# inefficient way of solving
a=[4, 2, 7, 1, 45, 23]
# def select_sort(x):
#     for i in range(len(x)-1):
#         # inefficient
#         y=x[i:] # each time through the loop look for the minimum from position i to the end.
        
#         # inefficient
#         m=min(y)
#         pos=x.index(m,i,len(x)) # find the index of the first element with value m in the range [i,len(x)
#         x[i],x[pos]=x[pos],x[i] # swap the element at position i with the element at position pos

# select_sort(a)
# print(a)


# def select_sort(x):
#     for i in range(len(x)-1):
#         m=x[i]
#         pos=i
#         for j in range(i,len(x)):
#             if x[j]<m:
#                 m=x[j]
#                 pos=j
#     x[i],x[pos]=x[pos],x[i]

# select_sort(a)
# print(a)


def insertion_sort(arr):
 # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)


def binary_search(arr, val, start, end):
 """Find index to insert val within arr[start:end] via binary search."""
 while start < end:
    mid = (start + end) // 2
    if arr[mid] < val:
        start = mid + 1
    else:
        end = mid
 return start

def binary_insertion_sort(arr):
 for i in range(1, len(arr)):
    val = arr[i]
 # Find the position to insert the current element
    pos = binary_search(arr, val, 0, i)
    # Shift elements to the right to make space for the current element
    arr[pos+1:i+1] = arr[pos:i]
    # Insert the current element into its correct position
    arr[pos] = val
 return arr

# in place sort means using a constant amount of memory