# 99

# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n == 2:
#         return 2
#     if n > 2:
#         return f(n - 1) * f(n - 3)
#
#
# print(f(7))


# 596

# def f(n):
#     if n <= 3:
#         return n
#     if n > 3 and n % 3 == 0:
#         return n**3 + f(n - 1)
#     if n > 3 and n % 3 == 1:
#         return 4 + f(n // 3)
#     if n > 3 and n % 3 == 2:
#         return n**2 + f(n - 2)
#
#
# print(f(100))


# 608

# def f(n):
#     if n <= 10:
#         return n
#     if 10 < n <= 36:
#         return n // 4 + f(n - 10)
#     if n > 36:
#         return 2 * f(n - 5)
#
#
# print(f(100))


# 610

# def f(n):
#     if n == 1:
#         return 2
#     if n > 1:
#         return f(n - 1) + 5*(n**2)
#
#
# print(f(39))


# 610

# def f(n):
#     if n < 5:
#         return 1 + 2*n
#     if n >= 5 and n % 3 == 0:
#         return 2 * (n + 1) * f(n - 2)
#     if n >= 5 and n % 3 != 0:
#         return 2 * n + 1 + f(n - 1) + 2 * f(n - 2)
#
#
# print(f(15))


# 1199

# def f(n):
#     if n <= 1:
#         return 1
#     if n > 1 and n % 2 == 0:
#         return 3 * n + f(n - 1)
#     if n > 1 and n % 2 != 0:
#         return 2 * f(n - 2)
#
#
# print(f(31))


# 1020

# def f(n):
#     if n <= 3:
#         return 3
#     if n > 3 and n % 2 == 0:
#         return f(n // 2) + 5
#     if n > 3 and n % 2 != 0:
#         return f(n - 1) - f(n - 2)
#
#
# print(f(20))


# 1408

# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return int((n + f(n - 2))/5)
#     if n > 2 and n % 2 != 0:
#         return int((2*n + f(n - 1) + f(n - 2))/4)
#
#
# print(f(50))


# 1860

# def f(n):
#     if n <= 1:
#         return 0
#     if n > 1 and n % 2 != 0:
#         return f(n - 1) + 3*n**2
#     if n > 1 and n % 2 == 0:
#         return n//2 + f(n - 1) + 2
#
#
# print(f(49))


# def f(n):
#     if n == 1:
#         return n
#     if n > 1:
#         return f(n - 1) - n * g(n - 1)
#
#
# def g(n):
#     if n == 1:
#         return n
#     if n > 1:
#         return f(n - 1) + 2 * g(n - 1)
#
#
# print(g(18))


# 593
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) - 2 * g(n - 1)
#
#
# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + g(n - 1) + n
#
#
# s = 0
# for x in str(g(36)):
#     s += int(x)
#
# print(s)


# 593
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n > 1:
#         return f(n - 1) - f(n - 2) + 3*n
#
#
# print(f(40))


# 628

# def f(n):
#     if n <= 18:
#         return n + 3
#     if n > 18 and n % 3 == 0:
#         return (n // 3) * f(n // 3) + n - 12
#     if n > 18 and n % 3 != 0:
#         return f(n - 1) + n**2 + 5
#
#
# k = 0
# for i in range(1, 1_001):
#     r = f(i)
#     a = [int(x) for x in str(r) if int(x) % 2 == 0]
#     if len(a) == len(str(r)):
#         k += 1

# print(k)


# 673

# def f(n):
#     if n > 30:
#         return n**2 + 5*n + 4
#     if n % 2 == 0 and n <= 30:
#         return f(n + 1) + 3 * f(n + 4)
#     if n % 2 != 0 and n <= 30:
#         return 2 * f(n + 2) + f(n + 5)
#
#
# k = 0
# for i in range(1, 1_001):
#     if sum([int(x) for x in str(f(i))]) == 27:
#         k += 1
# print(k)


# 2237

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n//2)
#     if n % 2 != 0:
#         return 1 + f(n - 1)
#
#
# k = 0
# for i in range(1, 501):
#     if f(i) == 8:
#         k += 1
#
# print(k)


# 1131

# def f(n):
#     if n == 1:
#         return 1
#     if n >= 2 and n % 2 == 0:
#         return f(n//2) + 1
#     if n >= 2 and n % 2 != 0:
#         return f(n - 1) + n
#
#
# for n in range(1, 1000):
#     if f(n) == 19:
#         print(n)


# 601

# def f(n, k=[]):
#     # print('*')
#     k.append(1)
#     if n >= 1:
#         # print('*')
#         k.append(1)
#         f(n - 1)
#         f(n - 3)
#         # print('*')
#         k.append(1)
#     return k
#
#
# print(sum(f(40)))


# 605

# def f(n, k=[]):
#     # print(n * n)
#     k.append(n * n)
#     if n > 1:
#         # print(2 * n + 1)
#         k.append(2 * n + 1)
#         f(n - 2)
#         f(n // 3)
#     return k
#
#
# print(sum(f(100)))


# 2248

# def f(n):
#     if n <= 1:
#         return n
#     if n > 1 and n % 3 == 0:
#         return n + f(n//3)
#     if n > 1 and n % 3 != 0:
#         return n + f(n + 3)
#
#
# for n in range(1, 100):
#     try:
#         if f(n) > 100:
#             print(n)
#     except:
#         pass


# 2247

# def f(n):
#     if n < 3:
#         return n + 1
#     if n >= 3 and n % 2 == 0:
#         return f(n - 2) + n - 2
#     if n >= 3 and n % 2 != 0:
#         return f(n + 2) + n + 2
#
#
# k = 0
# for x in range(1, 1000):
#     try:
#         if len(str(f(x))) == 5:
#             k += 1
#             # print(x)
#     except:
#         pass
# print(k)


# 2 ЧАСТЬ

# 4704

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 0:
#         return n * f(n - 1)
#
#
# for x in range(2024):
#     f(x)
#
# print(f(2023)//f(2020))


# 5155

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n**2 + f(n - 1)
#
#
# for x in range(1001):
#     f(x)
#
# print(f(1000) - f(997))


# 5154

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n > 100_000:
#         return n
#     if n <= 100_000:
#         return f(n + 1) + 5*n + 2
#
#
# for x in range(100000, 1, -1):
#     f(x)
#
# print(f(3) - f(7))


# 5156

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n <= 3:
#         return n
#     if n > 3 and n % 2 != 0:
#         return 2*n + f(n - 2)
#     if n > 3 and n % 2 == 0:
#         return n**2 + f(n - 1)
#
#
# for x in range(1, 100000):
#     f(x)
#
# print(f(10_000) - f(9_995))


# 5157
#
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n >= 10_000:
#         return n
#     if n < 10_000 and n % 3 == 0:
#         return n + f(n//3)
#     if n < 10_000 and n % 3 != 0:
#         return 2 * n + f(n + 3)
#
#
# for x in range(100_000, 1, -1):
#     try:
#         f(x)
#     except:
#         pass
#
# print(f(999) - f(46))


# 4733
#
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (2*n - 1) * f(n - 1)
#
#
# for x in range(1, 100000):
#     f(x)
#
# print(f(3516)/f(3513))


# 4740
#
# from functools import lru_cache
#
#
# def fact(n):
#     k = 1
#     for i in range(1, n + 1):
#         k *= i
#     return k
#
#
# @lru_cache(None)
# def f(n):
#     if n >= 5_000:
#         return fact(n)
#     if 1 <= n <= 5_000:
#         return 2 * f(n + 1)//(n + 1)
#
#
# for x in range(5_000, 1, -1):
#     f(x)
#
#
# print(1_000 * f(7) / f(4))


# 4739
#
# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n > 10_000:
#         return n - 10_000
#     if 1 <= n <= 10_000:
#         return f(n + 1) + f(n + 2)
#
#
# for x in range(100_000, 1, -1):
#     f(x)
#
#
# print(f(12_345) * ((f(10) - f(12)) // f(11)) + f(10_101))


# 5152

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 2
#     if n > 1:
#         return 2 * f(n - 1)
#
#
# for x in range(1, 100_000):
#     f(x)
#
# print(f(1900) // 2**1890)


# 5153

from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 != 0:
        return n
    if n > 3 and n % 2 == 0:
        return f(n - 1) + f(n - 2) + f(n - 3)


for x in range(1, 100_000):
    f(x)

print(f(2254) - f(2252))



