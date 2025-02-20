#Variant 1
def main(m, n):
    itr1 = 0
    for j in range(1, n+1):
        itr2 = 0
        for c in range(1, m+1):
            term1 = 26 * j**2
            term2 = 5 * c**3
            term3 = (j - (38 * j**2)) ** 7
            itr2 += term1 - term2 - term3
        itr1 += itr2
    return itr1


#Variant 2
def main(m, n):
    sum_j = sum(26 * j**2 - (j - 38 * j**2) ** 7 for j in range(1, n + 1))
    sum_c = sum(5 * c**3 for c in range(1, m + 1))
    return sum_j * m - sum_c * n

#Variant 3
def main(m, n):
    sum_j = sum(map(lambda j: 26 * j**2 - (j - 38 * j**2) ** 7, range(1, n + 1)))
    sum_c = sum(map(lambda c: 5 * c**3, range(1, m + 1)))
    return sum_j * m - sum_c * n


#Variant 4
def main(m, n):
    sum_j = 0
    j = 1
    while j <= n:
        term1 = 26 * j**2
        term2 = (j - 38 * j**2) ** 7
        sum_j += term1 - term2
        j += 1

    sum_c = 0
    c = 1
    while c <= m:
        term3 = 5 * c**3
        sum_c += term3
        c += 1

    return sum_j * m - sum_c * n

#Variant 5
def sum_j(n):
    if n == 0:
        return 0
    return (26 * n**2 - (n - 38 * n**2) ** 7) + sum_j(n - 1)

def sum_c(m):
    if m == 0:
        return 0
    return 5 * m**3 + sum_c(m - 1)

def main(m, n):
    return sum_j(n) * m - sum_c(m) * n
