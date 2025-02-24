# Variant 1
from cmath import sin


def main(n: int):
    if n >= 2:
        return (
            main(n - 1)
            - 13 * sin((main(n - 2) / 22) + 1 + (main(n - 2) ** 2 / 54)) ** 2
        ).real
    if n:
        return 0.11
    else:
        return -0.70


# Variant 2
from math import sin


def main(n: int):
    prev, curr = -0.70, 0.11
    for i, _ in enumerate(range(2, n + 1), 2):
        prev, curr = curr, curr - 13 * sin((prev / 22) + 1 + (prev**2 / 54)) ** 2
    return curr


# Variant 3
from cmath import sin


def main(n: int):

    def generator():
        a, b = -0.70, 0.11
        yield a
        yield b
        for _ in range(2, n + 1):
            a, b = b, (b - 13 * sin((a / 22) + 1 + (a**2 / 54)) ** 2).real
            yield b

    return list(generator())[-1]


# Variant 4
from math import sin


def main(n: int):
    prev, curr = -0.70, 0.11
    match n:
        case 0:
            return prev
        case 1:
            return curr
        case _:
            for i in range(2, n + 1):
                prev, curr = (
                    curr,
                    curr - 13 * sin((prev / 22) + 1 + (prev**2 / 54)) ** 2,
                )
            return curr


# Variant 5


def main(n):
    prev, curr = -0.70, 0.11
    for i in range(2, n + 1):
        prev, curr = curr, (
            curr - 13 * sin((prev / 22) + 1 + (prev**2 / 54)) ** 2
            if i % 2 == 0
            else curr
        )
    return curr
