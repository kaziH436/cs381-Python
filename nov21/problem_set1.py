def compose(*funcs):
    def composed(x):
        result = x
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed


def is_palindrome(s: str) -> bool: # STOP ONCE THEY MEET
    s = s.lower()
    return s == s[::-1]


def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def rotate_list(items: list, k: int) -> None:
   n = len(items)

   for _ in range(k):
      for i in range(n - 1, 0, -1):
         items[i], items[i - 1] = items[i - 1], items[i]


# This approach isn't truly in-place since it creates a new list slice,
# but it accomplishes the task of mutating the original list.
def rotate_list(items: list, k: int) -> None:
    n = len(items)
    k = k % n  # Handle cases where k > n
    items[:] = items[-k:] + items[:-k]

# def make_counter(start=0):
#     count = start
#     initial = start
#     history = []

#     def adjust(amount=1):
#         nonlocal count
#         history.append(count)
#         count += amount

#         return count

#     def reset():
#         nonlocal count
#         history.clear()
#         count = initial

#         return count

#     def undo():
#         nonlocal count
#         if history:
#             count = history.pop()

#         return count

#     return adjust, reset, undo




# No, deleting the variable a itself would not affect b. del a removes the reference a, not the list object. The list object still exists in memory and is referenced by b. After del a, you cannot access the list through a, but b still holds a reference to the list and can access it normally.


# def remove_every_nth_element(elements: list[int], n: int) -> None:
#     i = n - 1  # Start at the n-th element (0-indexed)
#     while i < len(elements):
#         del elements[i]
#         i += n - 1  # Move to the next n-th element (The -1 accounts for the deletion)


# def flatten(mylist: list) -> list:
#     result = []
#     for item in mylist:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result


# def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
#     result = []
#     i, j = 0, 0

#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             result.append(list1[i])
#             i += 1
#         else:
#             result.append(list2[j])
#             j += 1

#    # at this point either i or j is at the end of its list, so we can just blindly add the rest for both lists
#     result.extend(list1[i:])
#     result.extend(list2[j:])

#     return result