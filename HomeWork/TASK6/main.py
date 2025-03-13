# Variant 1
def main(psi_set):
    B = {psi // 5 - psi % 2 for psi in psi_set if -96 < psi <= 63}
    Xi = {abs(beta) for beta in B if -48 < beta <= 81}
    Theta = {psi // 6 for psi in psi_set if 43 < psi or psi <= -43}
    N = {theta % 3 - abs(theta) for theta in Theta if -88 < theta <= 65}
    omega = len(N) * len(Xi)
    sum_term = sum(nu + 4 * xi for nu in N for xi in Xi)
    omega += sum_term
    return omega


# Variant 2
def main(psi_set):
    B, Theta = set(), set()
    for psi in psi_set:
        if -96 < psi <= 63:
            B.add(psi // 5 - psi % 2)
        if psi > 43 or psi <= -43:
            Theta.add(psi // 6)
    Xi = {abs(beta) for beta in B if -48 < beta <= 81}
    N = {theta % 3 - abs(theta) for theta in Theta if -88 < theta <= 65}
    return len(N) * len(Xi) + sum(nu + 4 * xi for nu in N for xi in Xi)
