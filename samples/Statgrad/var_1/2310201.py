# 2
# from itertools import *
#
#
# def f(u, w, x, y, z):
#     return ((x <= y) and (z == (not w))) <= (u == (x or z))
#
#
# for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
#     table = [(0, a1, 0, 0, 0), (0, a2, a3, 0, 0), (a4, 0, 0, 0, a5), (a6, 0, a7, a8, 0)]
#     if len(set(table)) == len(table):
#         for a in permutations('uwxyz'):
#             if [f(**dict(zip(a, t))) for t in table] == [0, 0, 0, 0]:
#                 print(a)


# 5

# a = []
# for n in range(100):
#     b = bin(n)[2:]
#     n_b = b + bin(n % 4)[2:]
#     r = int(n_b, 2)
#     if r <= 49:
#         a.append(r)
#     # print(n, r)
# print(sorted(a))
# print(len(sorted(a)))


# 7
# a = (1024 * 768 * 12 * 0.8)
# b = (8 * 1024 * 200)
# print(a/b)


# 8

# from itertools import *
#
# k = 0
# for x in product('12345678', repeat=11):
#     s = ''.join(x)
#     if '0' not in s:
#         if (int(s[0]) % 2) != (int(s[1]) % 2) != (int(s[2]) % 2) != (int(s[3]) % 2) != (int(s[4]) % 2) != (int(s[5]) % 2) != (int(s[6]) % 2) != (int(s[7]) % 2) != (int(s[8]) % 2) != (int(s[9]) % 2) != (int(s[10]) % 2):
#             if s.count('1') <= 4 and s.count('2') <= 4 and s.count('3') <= 4 and s.count('4') <= 4 and s.count('5') <= 4 and s.count('6') <= 4 and s.count('7') <= 4 and s.count('8') <= 4:
#                 k += 1
# print(k)


from itertools import *

# k = 0
# for x in product('12345678', repeat=11):
#     s = ''.join(x)
#     for i in range(len(s)-1):
#         if (int(s[i]) % 2 != int(s[i+1]) % 2) and s.count(s[i]) <= 4:
#             print(s)
#             k += 1
# print(k)


# 9

# k = 0
# for s in open('09.txt'):
#     a = [int(x) for x in s.split()]
#     a_2 = [x for x in a if a.count(x) > 1]
#     if len(a_2) > 0 and max(a) not in a_2 and sum(a_2) > max(a):
#         k += 1
# print(k)


# 10

# k = 0
# for s in open('10.txt'):
#     a = [str(x) for x in s.split() if len(str(x)) == 3]
#     k += len(a)
# print(k)


# 11
# print((32768*560)/1024)


# 12

# for x1 in range(1, 15):
#     for x2 in range(1, 15):
#         for x3 in range(1, 15):
#             a = c = '0' + '1'*x1 + '2'*x2 + '3'*x3 + '0'
#
#             while '00' not in a:
#                 a = a.replace('01', '220', 1)
#                 a = a.replace('02', '1013', 1)
#                 a = a.replace('03', '120', 1)
#
#             if a.count('1') == 13 and a.count('2') == 18:
#                 print(a, 'длина A:', len(c))


# 13

# from ipaddress import *
#
# for mask in range(33):
#     net1 = ip_network(f'120.91.176.213/{mask}', 0)
#     net2 = ip_network(f'120.91.174.205/{mask}', 0)
#
#     if net1 != net2:
#         print(net1.netmask, net2.netmask)


# 14
#
# for x in range(40):
#     for y in range(40):
#         a = 9 + 1 * 40 + y * 40**2 + 2 * 40**3 + 9 * 40**4 + 6 * 40**5 + x * 40**6 + 7 * 40**7 + 5 * 40**8
#         if a % 39 == 0 and ((x*y)**0.5)**2 == x*y:
#             print(y*x)


# 15
#
# def f(x):
#     return ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)
#
#
# for a in range(1000):
#     if all(f(x) for x in range(10000)):
#         print(a)


# 16

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n//10) + n % 10
#     if n % 2 != 0:
#         return f(n//10)
#
#
# c = 0
# for k in range(2*10**9, 10**9 + 1, -1):
#     if f(k) == 0:
#         c += 1
#
#
# print(c)


# 17
# a = [int(x) for x in open('17.txt')]
#
# a123 = [x for x in a if len(str(x)) >= 3 and str(x)[-3] + str(x)[-2] + str(x)[-1] == '123']
#
# s = []
#
# for i in range(len(a)-2):
#     if (len(str(a[i])) == 5) + (len(str(a[i+1])) == 5) + (len(str(a[i+2])) == 5) >= 2:
#         if (a[i] % 3 == 0) + (a[i+1] % 3 == 0) + (a[i+2] % 3 == 0) == 1:
#             if a[i] + a[i+1] + a[i+2] > max(a123):
#                 s.append(a[i] + a[i+1] + a[i+2])
# print(len(s), max(s))


# 19-21
# def f(s, m):
#     if s >= 96:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     if s % 2 == 0 and s % 3 == 0:
#         h = [f(s + 1, m - 1), f(s + s//2, m - 1), f(s + s//3, m - 1)]
#     elif s % 3 == 0:
#         h = [f(s + 1, m - 1), f(s + s//3, m - 1)]
#     elif s % 2 == 0:
#         h = [f(s + 1, m - 1), f(s + s//2, m - 1)]
#     elif s % 2 != 0 and s % 3 != 0:
#         h = [f(s + 1, m - 1), f(s*2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19)', [s for s in range(1, 96) if f(s, 2)])
# print('20)', [s for s in range(1, 96) if not f(s, 1) and f(s, 3)])
# print('21)', [s for s in range(1, 96) if not f(s, 2) and f(s, 4)])


# 23
from functools import lru_cache
# from sys import setrecursionlimit
#
# setrecursionlimit(20000)
#
#
# @lru_cache(None)
# def f(curr, end, a):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if a == 'A' and curr < end:
#         return f(curr * 2, end, '') + f(curr * 3, end, '')
#     if a == '' and curr < end:
#         return f(curr - 1, end, 'A') + f(curr * 2, end, '') + f(curr * 3, end, '')
#
#
# print(f(3, 20, ''))


# 24
# s = open('24.txt').readline()

# a = 0
# b = 0
# k = m = 0
# for i in range(len(s)):
#     if s[i] == 'A':
#         a += 1
#     if s[i] == 'B':
#         b += 1
#     if a <= 2 and b <= 2:
#         k += 1
#         m = max(m, k)
#     elif a > 2 or b > 2:
#         k = 0
#         a = 0
#         b = 0
#     print(a, b, k, m)
# print(m)















