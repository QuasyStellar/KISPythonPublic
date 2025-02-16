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

if __name__ == "__main__":
    print(main(102))
