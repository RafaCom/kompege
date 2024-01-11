# 59

# def f(x):
#     return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)
#
#
# for a in range(1, 100):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         print(a)


# 432

# def f(x):
#     return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)
#
#
# for a in range(1, 30000):
#     if all(f(x) for x in range(1, 30000)):
#         print(a)


# 764

# def f(x):
#     return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))
#
#
# for a in range(1, 1000):
#     if all(f(x) for x in range(1, 10000)):
#         print(a)


# 948

# def f(x):
#     return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)
#
#
# for a in range(1, 1000):
#     if all(f(x) for x in range(1, 10000)):
#         print(a)


# 1127

# def f(x):
#     return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))
#
#
# for a in range(1, 3000):
#     if all(f(x) for x in range(1, 300000)):
#         print(a)


# 216

# def f(x):
#     return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))
#
#
# for a in range(1, 1000):
#     if all(f(x) for x in range(1, 100000)):
#         print(a)


# 2078

# def f(x):
#     return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))
#
#
# for a in range(1, 10000):
#     if all(f(x) for x in range(1, 100000)):
#         print(a)


# 2079

# def f(x):
#     return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))
#
#
# for a in range(1, 1000):
#     if all(f(x) for x in range(1, 10000)):
#         print(a)


# 2081

# from itertools import *
#
# p = set()
# q = set()
# a = set()
#
# for i in product('01', repeat=8):
#     s = ''.join(i)
#     if s[0] == '1' and s[1] == '1':
#         p.add(s)
#
# for i in product('01', repeat=8):
#     s = ''.join(i)
#     if s[-1] == '0':
#         q.add(s)
#
#
# def f(x):
#     return (not (x in a)) <= ((x in p) or (not (x in q)))
#
#
# for x in product('01', repeat=8):
#     s = ''.join(x)
#     if f(s) == 0:
#         a.add(s)
#
# print(len(a))


# 627


# def f(x, y):
#     return (x * y > a) and (x > y) and (x < 8)
#
#
# for a in range(300):
#     if all(f(x, y) == 0 for x in range(3000) for y in range(3000)):
#         print(a)


# 1015

# def f(x, y):
#     return (x > 39) or (y > 26) or (2*x + 4*y < a)
#
#
# for a in range(1, 1000):
#     if all(f(x, y) for x in range(1, 10000) for y in range(1, 10000)):
#         print(a)


# 1859

# def f(x, y):
#     return (2*x + y != 70) or (x < y) or (a < x)
#
#
# for a in range(1, 100):
#     if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)


# 2080

# def f(x, y):
#     return (x**2 - 10*x + 16 > 0) or (y**2 -10*y + 21 > 0) or (x*y < 2*a)
#
#
# for a in range(1000):
#     if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)


# 743

# b = {1, 3, 5, 7, 9, 11}
# c = {3, 6, 9, 12}
# a = set()


# def f(x):
#     return ((x in b) <= (not (x in c)) or (x in a))
#
#
# for x in range(10000):
#     if f(x) == 0:
#         a.add(x)
#
# print(sum(a))


# 752

# A = set()
# B = {3, 6, 9, 12}
# C = {1, 2, 3, 4, 5, 6}
#
#
# def f(x):
#     return (not ((not (x in A)) and (x in B))) or (not (x in C))
#
#
# for x in range(1000):
#     if f(x) == 0:
#         A.add(x)
#
# print(len(A))


# 754

# A = set(range(1000))
# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
#
#
# def f(x):
#     return ((x in A) <= (x in P)) and ((x in Q) <= (not (x in A)))
#
#
# for x in range(1000):
#     if f(x) == 0:
#         A.remove(x)
#
# print(len(A))


# 1409

# A = set()
# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# R = {12, 24, 36, 48, 60}
#
#
# def f(x):
#     return (x not in A) <= (((x in P) and (x in Q)) <= (x in R))
#
#
# for x in range(1000):
#     if f(x) == 0:
#         A.add(x)
#
# print(A)
# print(18 * 6)


# 1968
#
# from itertools import *
#
# def f(x):
#     D = 17 <= x <= 58
#     C = 29 <= x <= 80
#     A = a1 <= x <= a2
#     return D <= (((not C) and (not A)) <= (not D))
#
#
# Ox = [i/4 for i in range(16*4, 81*4+1)]
# m = []
#
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in Ox):
#         m.append(a2 - a1)
#
# print(min(m))


#  1295
# from itertools import *
#
#
# def f(x):
#     P = 17 <= x <= 54
#     Q = 37 <= x <= 83
#     A = a1 <= x <= a2
#     return P <= ((Q and (not A)) <= (not P))
#
# Ox = [i/4 for i in range(16*4, 84*4)]
# m = []
#
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in range(100)):
#         m.append(a2 - a1)
#
# print(min(m))


# 1198

from itertools import *


# def f(x):
#     B = 18 <= x <= 52
#     C = 16 <= x <= 41
#     A = a1 <= x <= a2
#     return (B <= A) and ((not C) or A)
#
#
# Ox = [i/4 for i in range(15*4, 53*4)]
# m = []
#
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in Ox):
#         print(a1, a2)
#         m.append(a2 - a1)
#
# print(min(m))



