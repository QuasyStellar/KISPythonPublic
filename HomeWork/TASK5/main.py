#Varian 1
def main(z, y):
    n = len(y)
    s = 0
    for i in range(1, n + 1):
        s += 21 * (y[n - i] + z[i // 3] ** 2)
    return 62 * s

#Variant 2
def main(z, y):
    n = len(y)
    return 62 * sum(21 * (y[n - i] + z[i // 3] ** 2)
                    for i in range(1, n + 1))

#Variant 3
def main(z, y):
    n = len(y)
    i = 1
    s = 0
    while i <= n:
        s += 21 * (y[n - i] + z[i // 3] ** 2)
        i += 1
    return 62 * s
