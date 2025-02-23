# Varian 1
# import math
#
# def main(z, y) -> float:
#     part1 = math.sqrt(48) * abs((y**3) / 30 - z - 31)
#     part2 = 14 * (88 * z**2 - 97 * y**3)**4
#     return part1 + part2

# Variant 2
# import math
#
#
# def calc_sqr(A):
#     return math.sqrt(48) * abs(A)
#
#
# def calc_rht(z, y):
#     return 14 * (88 * z**2 - 97 * y**3) ** 4
#
#
# def main(z, y) -> float:
#     return calc_sqr((y**3) / 30 - z - 31) + calc_rht(z, y)

# Variant 3
# def main(z, y) -> float:
#     sqr = (48 * ((y**3) / 30 - z - 31) ** 2) ** 0.5
#     rht = 14 * (88 * z**2 - 97 * y**3) ** 4
#     return sqr + rht

# Variant 4
from functools import reduce


def add(x, y):
    return x + y


def main(z, y) -> float:
    return reduce(
        add,
        [(48 * ((y**3 / 30 - z - 31) ** 2)) ** 0.5, 14 * (88 * z**2 - 97 * y**3) ** 4],
    )
