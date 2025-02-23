# Variant 1
# def main(y):
#     if y < 147:
#         return (y**3 / 65) ** 5 - y**3
#     if 147 <= y < 192:
#         return y**2 - 1 - 15 * (y**0.5) ** 3
#     if 192 <= y < 214:
#         return 25 * y**6
#     if 214 <= y < 259:
#         return 82 + y**2
#     return 56 * y**6

# Variant 2
# def main(y):
#     conditions = [
#         (y < 147, (y**3 / 65) ** 5 - y**3),
#         (147 <= y < 192, y**2 - 1 - 15 * (y**0.5) ** 3),
#         (192 <= y < 214, 25 * y**6),
#         (214 <= y < 259, 82 + y**2),
#         (y >= 259, 56 * y**6),
#     ]
#     return next(result for condition, result in conditions if condition)

# Variant 3
# import bisect
#
#
# def main(y):
#     thresholds = [147, 192, 214, 259]
#     functions = [
#         lambda y: (y**3 / 65) ** 5 - y**3,
#         lambda y: y**2 - 1 - 15 * (y**0.5) ** 3,
#         lambda y: 25 * y**6,
#         lambda y: 82 + y**2,
#         lambda y: 56 * y**6,
#     ]
#
#     idx = bisect.bisect_right(thresholds, y)
#     return functions[idx](y)
#

if __name__ == "__main__":
    print(main(102))
