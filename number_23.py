# 413
#
# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr + 3, end) + f(curr * 2, end)
#
#
# print(f(1, 15))


# 633

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr * 2, end) + f(curr ** 2, end)
#
#
# print(f(5, 154))


# 2344

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr + 2, end) + f(curr * 4, end)
#
#
# print(f(1, 13))


# 1301

# def f(curr, end):
#     if curr < end:
#         return 0
#     if curr == end:
#         return 1
#     if curr > end:
#         return f(curr - 2, end) + f(curr - 5, end)
#
#
# print(f(23, 2))


# 2345

# def f(curr, end):
#     if curr < end:
#         return 0
#     if curr == end:
#         return 1
#     if curr > end:
#         return f(curr - 1, end) + f(curr - 3, end) + f(curr // 3, end)
#
#
# print(f(22, 2))


# 20

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr * 2, end)
#
#
# print(f(1, 10) * f(10, 20))


# 1037

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr * 2, end)
#
#
# print(f(1, 12) * f(12, 30))


# 65

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr + 3, end) + f(curr * 2, end)
#
#
# print(f(3, 9) * f(9, 12) * f(12, 20))


# 1376

# def f(curr, end):
#     if curr < end:
#         return 0
#     if curr == end:
#         return 1
#     if curr > end:
#         return f(curr - 8, end) + f(curr // 2, end)
#
#
# print(f(102, 43) * f(43, 5))


# 222

# def f(curr, end):
#     if curr > end or curr == 6:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 2, end) + f(curr * 3, end)
#
#
# print(f(1, 25) * f(25, 63))


# 951

# def f(curr, end):
#     if curr > end or curr == 11 or curr == 18:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr + 2, end) + f(curr * 3, end)
#
#
# print(f(4, 8) * f(8, 23))


# 104

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 1, end) + f(curr * 2, end) + f(curr * 2 + 1, end) + f(curr * 10, end)
#
#
# print(f(1, 15))


# 473

# def f(curr, end):
#     if curr > end or curr == 43:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         return f(curr + 2, end) + f(curr + curr - 1, end) + f(curr + curr + 1, end)
#
#
# print(f(7, 63))


# 1137

# def f(curr, end):
#     if curr > end:
#         return 0
#     if curr == end:
#         return 1
#     if curr < end:
#         curr = bin(curr)[2:]
#         return f(int(curr, 2) + 1, end) + f(int(curr + '0', 2), end) + f(int(curr + '1', 2), end)
#
#
# print(f(4, 29))


# 2342

# def f(c, e):
#     if c > e:
#         return 0
#     if c == e:
#         return 1
#     if c < e and '9' != str(c)[1]:
#         return f(c + 1, e) + f(c + 11, e)
#     if c < e and '9' == str(c)[1]:
#         return f(c + 1, e) + f(c + 10, e)
#
#
# print(f(25, 51))


# 2343

# def f(c, e):
#     if c > e:
#         return 0
#     if c == e:
#         return 1
#     if c < e and c % 2 == 0:
#         return f(c + 1, e) + f(c * 1.5, e)
#     if c < e and c % 2 != 0:
#         return f(c + 1, e)
#
#
# print(f(1, 20))


# 2340

# def f(c, e):
#     if c > e:
#         return 0
#     if c == e:
#         return 1
#     if c < e:
#         return f(c + 2, e) + f(c + 4, e) + f(c + 5, e)
#
#
# for i in range(1, 100):
#     if f(31, i) == 1001:
#         print(i)


# 886

# def f(c, e, step):
#     if c > e:
#         return 0
#     if c == e and step != 7:
#         return 0
#     if c == e and step == 7:
#         return 1
#     if c < e:
#         return f(c + 1, e, step+1) + f(c + 4, e, step+1) + f(c * 2, e, step+1)
#
#
# print(f(3, 27, 0))


# 2339

# a = set()
#
#
# def f(c, step):
#     if step == 15:
#         print(c)
#         a.add(c)
#     else:
#         f(c * 2, step + 1)
#         f(c * 2 + 1, step + 1)
#
#
# f(1, 0)
# print(len(a))


# 2341

# a = set()
#
#
# def f(c, step):
#     if step == 8:
#         if 1000 <= c <= 1024:
#             a.add(c)
#     else:
#         f(c + 1, step + 1)
#         f(c + 5, step + 1)
#         f(c * 3, step + 1)
#
#
# f(1, 0)
# print(len(a))


# 3030

# def f(c, e, p):
#     if c > e:
#         return 0
#     if c == e:
#         return 1
#     if c < e and p != "*2":
#         return f(c + 1, e, "+1") + f(c + 2, e, "+2") + f(c * 2, e, "*2")
#     if c < e and p == "*2":
#         return f(c + 1, e, "+1") + f(c + 2, e, "+2")
#
#
# print(f(1, 15, ''))


# 3162

# def f(c, e, k):
#     if c > e:
#         return 0
#     if c == e:
#         return k == 1
#     if c < e:
#         return f(c + 1, e, k) + f(c + 2, e, k) + f(c * 2, e, k + 1)
#
#
# print(f(2, 12, 0))


# 4275

# def f(c, e, k):
#     if c > e:
#         return 0
#     if c == e:
#         return k <= 3
#     if c < e:
#         return f(c + 2, e, k) + f(c * 3, e, k + 1) + f(c * 5, e, k + 1)
#
#
# print(f(2, 200, 0))


# 4492

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(c, e, k):
#     if c % 2 != 0:
#         k += 1
#     if c > e:
#         return 0
#     if c == e:
#         return k == 1
#     if c < e:
#         return f(c + 1, e, k) + f(c + 2, e, k) + f(c * 2, e, k)
#
#
# print(f(2, 40, 0))


# 2714

# def f(c, e, k):
#     if c % 2 == 0:
#         k += 1
#     if c > e:
#         return 0
#     if c == e:
#         return k == 6
#     if c < e:
#         return f(c + 1, e, k) + f(c + 3, e, k) + f(c + 5, e, k)
#
#
# print(f(3, 25, 0))





