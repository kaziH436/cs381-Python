def f(x):  # x is a list
    n=len(x)
    for i in range(n // 2):
        x[i], x[n-i-1] = x[n-i-1], x[i]
    return x


def get_values(*args): 
    return sum(args), max(args), min(args)


def sort_list_of_lists_by_average(x):
    return sorted(x, key=lambda sub: sum(sub) / len(sub))

