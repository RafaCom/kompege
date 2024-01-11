# n = 5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875
# a = []
#
# while n > 0:
#     a = [n % 6] + a
#     n //= 6
#
# print(a.count(5) - a.count(0))

# for x in range(50):
#     if (3 * 1 + 3 * (x+4)) - (3 * 1 + 3 * 4) == 33:
#         print(x)


# for n in range(100):
#     if 3 * 1 + 0 + 1 * n**2 == 7 * 1 + 9 * (n + 2):
#         print(n)


# for n in range(1, 100):
#     if 1 * n**2 + 3 * n + 2 * 1 + 1 * 8 + 3 * 1 == 4 * 1 + 2 * (n+1) + 1 * (n+1)**2:
#         print(n)


# for x in range(2, 1000):
#     if (1 + 2 * x) * (3 + 1 * x) == (3 + 1 * x + 3 * x**2):
#         print(x)


# for x in range(20, 31):
#     a = []
#     n = x
#     while n > 0:
#         a = [n % 3] + a
#         n //= 3
#     if a[-2] == 1 and a[-1] == 1:
#         print(x)

#
# for x in range(1, 41):
#     b = bin(x)[2:]
#     if len(b) >= 4 and b[-1] + b[-2] + b[-3] + b[-4] == '1101':
#         print(x)

# for n in range(2, 100):
#     t = 68
#     a = []
#     while t > 0:
#         a = [t % n] + a
#         t //= n
#     if len(a) == 4 and a[-1] == 2:
#         print(n)

# for n in range(1, 1000):
#     if 6 <= n < 36 and 25 <= n < 125 and n % 11 == 1:
#         print(n)


# def f(x, cc):
#     a = []
#
#     while x > 0:
#         a = [x % cc] + a
#         x //= cc
#
#     return a
#
#
# k = 0
# for x in range(1, 1000):
#     if len(f(x, 5)) <= 4 and len(f(x, 2)) >= 5 and f(x, 16)[-1] == 12:
#         k += 1
#         print(x, k)


# for x in range(15):
#     a = (5 + x * 15 + 3 * 15**2 + 2 * 15**3 + 1 * 15**4)
#     b = (3 + 3 * 15 + 2 * 15**2 + x * 15**3 + 1 * 15**4)
#     if (a+b) % 14 == 0:
#         print(x, (a+b)/14)


# for x in range(17):
#     a = x + 9 * 17 + 5 * 17**2 + 7 * 17**3 + 9 * 17**4
#     b = 8 + 1 * 17**2 + x * 17**3 + 3 * 17**4
#     c = a + b
#     if c % 11 == 0:
#         print(c/11)

# for z in range(14):
#     for y in range(12):
#         for x in range(11):
#             c = 7 + 8 * 14 + z * 14 ** 2 + 5 * 14 ** 3 + 5 * 14 ** 4
#             b = 6 + 4 * 12 + 9 * 12 ** 2 + 7 * 12 ** 3 + y * 12 ** 4
#             a = x + 4 * 11 + 6 * 11**2 + 3 * 11**3 + 3 * 11**4
#
#             if (a + b) == c:
#                 print(c)


# for x in range(17):
#     for y in range(15):
#         a = 5 + x * 15 + 3 * 15**2 + 2 * 15**3 + 1 * 15**4
#         b = 9 + y * 17 + 7 * 17**2 + 6 * 17**3
#         c = a + b
#
#         if c % 131 == 0:
#             print(x, y, c/131)


# for x in range(21):
#     for y in range(21):
#         a = 9 + x * 21 + y * 21**2 + 2 * 21**3 + 1 * 21**4
#         b = 9 + 9 * 21 + y * 21**2 + 6 * 21**3 + 3 * 21**4
#         c = a + b
#
#         if c % 18 == 0:
#             a = 9 + x * 21 + 5 * 21 ** 2 + 2 * 21 ** 3 + 1 * 21 ** 4
#             b = 9 + 9 * 21 + 5 * 21 ** 2 + 6 * 21 ** 3 + 3 * 21 ** 4
#             c = a + b
#             print(c/18)
