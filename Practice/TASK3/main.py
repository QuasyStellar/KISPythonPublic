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


def main(m, n):
    sum_j = sum(26 * j**2 - (j - 38 * j**2) ** 7 for j in range(1, n + 1))
    sum_c = sum(5 * c**3 for c in range(1, m + 1))
    return sum_j * m - sum_c * n


def main(m, n):
    sum_j = sum(map(lambda j: 26 * j**2 - (j - 38 * j**2) ** 7, range(1, n + 1)))
    sum_c = sum(map(lambda c: 5 * c**3, range(1, m + 1)))
    return sum_j * m - sum_c * n
