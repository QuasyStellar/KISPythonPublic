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


