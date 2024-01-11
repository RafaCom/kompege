# 2
# from itertools import *
#
#
# def f(w, x, y, z):
#     return ((x <= y) or (z <= w)) and (not(x <= w))
#
#
# for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
#     table = [(1, 0, 1, a1), (1, a2, a3, 1), (a4, a5, 1, 0)]
#     if len(table) == len(set(table)):
#         for x in permutations('wxyz'):
#             if [f(**dict(zip(x, t))) for t in table] == [0, 1, 1]:
#                 print(x)


# 5

# def cc3(x):
#     a = []
#     t = x
#     while t > 0:
#         a = [t % 3] + a
#         t //= 3
#     return a
#
#
# for n in range(10, 100):
#     b = cc3(n)
#     if n % 4 == 0:
#         b = b + [b[-3]] + [b[-2]] + [b[-1]]
#     else:
#         b = b + cc3((n % 4)*4)
#
#     str_list = [str(x) for x in b]
#     str_n = ''.join(str_list)
#     r = int(str_n, 3)
#     if r < 127:
#         print(r)


# 6

# from turtle import *
#
# screensize(1500, 1500)
# tracer(0)
# r = 6
#
# for n in range(45):
#     fd(15*r)
#     rt(24)
#
# up()

# update()
# exitonclick()


# 7
# a = (1200 * 640 * 9) * 512
# print(a / (8 * 1024 * 1024))


# 8
# from itertools import *
#
#
# k = 0
# a = set()
# for x in permutations('0123456789ABCDEFG', 6):
#     s = ''.join(x)
#     try:
#         if int(s[0]) % 2 == 0:
#             for i in s:
#                 for n in range(2, int(i) // 2 + 1):
#                     if int(i) % n != 0:
#                         a.add(s)

# except ValueError:
#     d = {'A': '10', 'B': "11", 'C': "12", "D": "13", "E": "14", "F": "15", "G": "16"}
#     if s[0] == 'A':
#         for i in s:
#             for n in range(2, int(i) // 2 + 1):
#                 if int(i) % n != 0:
#                     a.add(s)


# 9

# n = 0
# r = []
# for s in open('09.txt'):
#     n += 1
#     s = sorted([int(x) for x in s.split()])
#     a = [x for x in s if s.count(x) > 1]
#     if len(a) >= 1 and (sum(a) / len(a)) < (sum(s) / len(s)):
#         r.append(n)
# print(sum(r))


# 12

# for n in range(4, 1000):
#     s = '5' + n * '2'
#     while '52' in s or '222' in s or '122' in s:
#         if '52' in s:
#             s = s.replace('52', '11', 1)
#         if '222' in s:
#             s = s.replace('222', '15', 1)
#         if '122' in s:
#             s = s.replace('122', '21', 1)
#     a = [int(x) for x in s.split()]
#     k = 0
#     for x in s:
#         k += int(x)
#     if (int((k ** 0.5)))**2 == k:
#         print(n, a, k)


# 13
# from ipaddress import *
# k = 0
# net = ip_network('172.118.1.255/255.255.252.0', 0)
# for n in net:
#     b = f'{n:b}'
#     a = [int(i) for i in b]
#     if sum(a) in (11, 13, 17, 19):
#         k += 1
#         print(n, b, sum(a))
# print(k - 1)


# 14

# t = 5 * 3**1917 + 6 * 2**1878 + 7 * 3**1870 - 1991
# a = []
# print(t)
# while t > 0:
#     a = [t % 17] + a
#     t //= 17
# print(a)
#
# r = set()
# for x in a:
#     r.add(a.count(x))
#     print(a.count(x), x)
#
# print('')
# print(max(r))


# 15

# def f(x):
#     return (x & a != 0) or ((x & 52 == 0) and (x & 14 == 0))
#
#
# for a in range(1, 10000):
#     if all(f(x) for x in range(1, 100000)):
#         print(a)


# 16
# from functools import lru_cache
#
#
# @lru_cache(None)
# def h(x):
#     if x < 3:
#         return 1
#     if x > 2:
#         return 2*x - 1 + h(x - 2)
#
#
# for i in range(3034):
#     h(i)
#
# print(h(3033))


# 23

def f(c, e):
    if c > e or c == 13:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f(c + 5, e) + f(c * 2, e)


print(f(7, 25))
