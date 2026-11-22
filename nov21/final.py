def f(n):
    L = []
    for i in range(n):
        L.append(i)
        print(L)
        L.append([i])
        print(L)
        L.append(i)
        print(L)


z = [1, 2, 3, 2, 1, 2, 4, 5, 1, 4, 1]

def report(z):
    d = {}
    for i in range(len(z)):
        if z[i] not in d:
            d[z[i]] = [0, []]       # [count, positions]
        d[z[i]][0] += 1
        d[z[i]][1].append(i)
    for k in d:
        print("Element: " + str(k) + ", found " + str(d[k][0]) +
              " times, at positions " + ", ".join(str(p) for p in d[k][1]))

report(z)