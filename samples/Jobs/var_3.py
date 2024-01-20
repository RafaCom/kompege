# 2
# from itertools import *
#
#
# def f(x, y, z, w):
#     return (w or x or (not z) or y) and (w or x or (not z) or (not y)) and (w or (not x) or (not z) or (not y))
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(a1, a2, 1, a3), (a4, 1, 1, a5), (a6, 1, 1, 1)]
#     if len(set(table)) == len(table):
#         for x in permutations('xyzw'):
#             if [f(**dict(zip(x, t))) for t in table] == [0, 0, 0]:
#                 print(x)


# 5

# for n in range(1, 100):
#     b = bin(n)[2:]
#     s = []
#     for i in b:
#         s.append(int(i))
#     if sum(s) % 2 != 0:
#         b += '11'
#     else:
#         b = '11' + b
#     dec_n = int(b, 2)
#     if dec_n > 102:
#         print(n, dec_n)


# 8
# from itertools import product
#
# product_str = 'КЕГЭ2023'
#
# for i in sorted(product(product_str, repeat=4), key=lambda x: (not x.isdigit(), x)):
#     s = ''.join(i)
#     print(s)


# 9
# k = 0
# for i in open('09.txt'):
#     a = [int(x) for x in i.split()]
#     if sum(a) == 360:
#         k += 1
# print(k)


# 12

# m = []
# for n in range(101, 5000):
#     s = '3' * n
#     while '111' in s or '333' in s:
#         if '111' in s:
#             s = s.replace('111', '3', 1)
#         else:
#             s = s.replace('333', '1', 1)
#     if n > 100:
#         m.append(s)
#         print(n, s)
# print(n, min(m))


# 13

# from ipaddress import *
#
# k = 0
# net = ip_network('102.12.21.201/255.255.252.0', 0)
# for n in net:
#     b = f'{n:b}'
#     if b.count('1') % 2 == 0:
#         print(b)
#         k += 1
# print(k)


# 14

# t = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
# a = []
#
# while t > 0:
#     a = [t % 5] + a
#     t //= 5
# print(a.count(4))


# 15

# def f(x, y):
#     return (2*x + 3*y != 150) or (x < a) and (y < a)
#
#
# for a in range(1000):
#     if all(f(x, y) for x in range(10000) for y in range(10000)):
#         print(a)


# 16


# def f(n):
#     print(n)
#     if n < 5:
#         f(n + 1)
#         f(n + 2)
#
#
# f(2)
# print(2 + 3 + 4 + 5 + 6 + 5 + 4 + 5 + 6)


# 17

# a = [int(x) for x in open('17.txt')]
#
# ans = []
# a_17 = [x for x in a if x % 17 == 0]
# print(a_17)
#
# for i in range(len(a)-1):
#     if a[i] + a[i+1] > max(a_17):
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), max(ans))


# 19-21

# def f(a, b, m):
#     if a + b >= 57:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a+b, b, m - 1), f(a, a+b, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(100) if f(10, s, 2)])  # all => any
# print('20)', [s for s in range(100) if f(9, s, 3)])
# print('21)', [s1 for s1 in range(100) if f(s1, s1, 4)])


# 23

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr * 2, end) + f(curr * 3, end)
#
#
# print(f(8, 96) * f(96, 3456))


# 64 балла
