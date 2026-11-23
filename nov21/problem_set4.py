def reverse_slice(lst: list[int], start: int, end: int) -> list[int]:
    n = len(lst)

    # Empty list, or range lies entirely outside the list, or inverted range
    if n == 0 or start > end or end < 0 or start > n - 1:
        return []

    # Clamp the partially out-of-bounds cases
    start = max(start, 0)
    end = min(end, n - 1)

    result = []
    for i in range(end, start - 1, -1):
        result.append(lst[i])
    return result


def apply_transformation(numbers, transform_function):
    return [transform_function(x) for x in numbers]


mylist = sorted([5, 4, 21, 20, 39], key=lambda x: x % 10)
print(mylist)  # [20, 21, 4, 5, 39]


lst = [1, 2, 3, 4, 5]
lst[1:4:2] = [10, 20]
print(lst)


d = [4, 1, 6]
lst = [*d, *sorted(d)]
print(lst)


lst = [1, 2, 3, 4, 5]
new_lst = lst[::-1][:3][::-1]
print(new_lst)


# Output:

# [1, 2, 3, 4]
# [1, 2, 3]

# Explanation: The key here is numbers[:], which creates a shallow copy of the list. When func(numbers[:], 4) is called, the function receives a copy of the list, not the original. The function appends 4 to the copy and returns it. The original numbers list remains unchanged because the function modified only the copy, not the original.