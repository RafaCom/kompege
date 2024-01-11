from itertools import *


# def f(w, x, y, z):
#     return (x or (not y)) and (not (y == z)) and w
#
#
# for a1, a2, a3, a4 in product([0, 1], repeat=4):
#     table = [(0, 1, a1, 0), (a2, 1, 1, 0), (1, a3, 0, a4)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#                 print(p)


# def f(a, b, c):
#     return (a and (not c)) or (not b and not c)
#
#
# table = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
#
# for p in permutations('abc'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 0, 0, 0, 1, 0, 1, 0]:
#         print(p)


# def f(x, y, z):
#     return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
#
#
# table = [(0, 0, 0), (1, 0, 0), (1, 0, 1)]
#
# for p in permutations('xyz'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#         print(p)


# def f(x, y, z, w):
#     return (((not x) and y) == z) and w
#
#
# for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product([0, 1], repeat=10):
#     table = [(a1, 0, a2, a3), (a4, a5, a6, 0), (0, 0, a7, a8), (0, 0, a9, a10)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
#                 print(p)


# def f(x, y, z, w):
#     return (x <= (y and (not z))) or w
#
#
# s = set()
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(a1, a2, 1, 0), (0, a3, a4, 1), (1, a5, 1, a6)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 # print(p)
#                 s.add(p)
# print(s)


# def f(x, y, z, w):
#     return (x and (not y)) or (x == z) or w
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(1, a1, a2, 1), (a3, 0, a4, 0), (1, a5, 1, a6)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(x, y, z):
#     return ((not x) and y and z) or ((not x) and (not z))
#
#
# table = [(0, 0, 0), (1, 0, 0), (1, 1, 0)]
#
# for p in permutations('xyz'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#         print(p)


# def f(x, y, z, w):
#     return (not y) and x and ((not z) or w)
#
# table = [(0, 1, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0)]
#
# for p in permutations('xywz'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#         print(p)


# def f(x, y, z, w):
#     return (y <= x or z) and (z <= y)
#
#
# table = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 0, 1), (0, 1, 1, 0)]
#
# for p in permutations('xyzw'):
#     if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0, 0]:
#         print(p)


# def f(x, y, z):
#     return (not(x == (y <= z)))
#
#
# table = [(0, 0, 1), (0, 1, 1)]
#
# for p in permutations('xyz'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 0]:
#         print(p)


# def f(w, x, y, z):
#     return (y <= x) or (not((x <= z) and (z <= x))) and (not(w))
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(0, 0, 0, a1), (a2, 0, 0, a3), (a4, a5, 0, a6)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(w, x, y, z):
#     return (not w) and ((y or z) <= ((not x) and y))
#
#
# for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
#     table = [(a1, a2, a3, 1), (a4, a5, 1, a6), (a7, 1, 1, a8)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#                 print(p)


# def f(w, x, y, z):
#     return ((w <= y) or (not (y <= z))) and (not x) and (not (x == z))
#
#
# for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
#     table = [(0, a1, 1, a2), (1, a3, a4, 1), (0, a5, 1, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#                 print(p)


# def f(w, x, y, z):
#     return (x <= y) or (not(w <= z))
#
#
# table = [(1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 1, 1)]
#
# for p in permutations('wxyz'):
#     if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#         print(p)


# def f(a, b, c, d):
#     return ((a and b) == (not c)) and (b <= d)
#
#
# table = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0)]
#
# for p in permutations('abcd'):
#     if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
#         print(p)

#
# def f(w, x, y, z):
#     return (not (z and (not w))) or ((z <= w) == (x <= y))
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(1, a1, a2, a3), (1, 1, a4, 1), (1, a5, a6, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(a, b, c, d):
#     return ((not a) and (not b)) or (b == c) or d
#
#
# for a1, a2, a3, a4 in product([0, 1], repeat=4):
#     table = [(a1, a2, 1, a3), (1, 0, a4, 1), (0, 0, 1, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('abcd'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(x, y, z, w):
#     return ((z <= x) and (x <= w)) or (y == (z or x))
#
#
# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     table = [(a1, 1, a2, a3), (a4, a5, 1, 1), (a6, 1, a7, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(x, y, z, w):
#     return (x and z) or ((w <= x) == (z <= y))
#
#
# for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
#     table = [(a1, a2, a3, 1), (a4, a5, 1, 1), (a6, 1, 1, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(x, y, z, w):
#     return (x == (not z)) <= ((x or w) == y)
#
#
# for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
#     table = [(0, a1, 0, a2), (a3, a4, 0, 0), (a5, 0, 0, 0)]
#     if len(table) == len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


# def f(w, x, y, z):
#     return y and (x or z) or (not (y or z)) or w
#
#
# for a1, a2, a3, a4 in product([0, 1], repeat=4):
#     table = [(1, a1, 0, 1), (a2, 1, 0, a3), (0, 0, a4, 1)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
#                 print(p)


