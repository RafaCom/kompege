from itertools import *

# k = 0
# for x in product('01234', repeat=6):
#     s = ''.join(x)
#     if s[0] != '0' and s[0] != '1' and s[-1] != '3' and s[-1] != '4':
#         print(s)
#         k += 1
#
# print(k)

# k = 0
# for x in permutations('01234567', 5):
#     s = ''.join(x)
#     if s[0] != '0' and '1' not in s:
#         s = s.replace('2', '0').replace('3', '1').replace('4', '0').replace('5', '1').replace('6', '0').replace('7', '1')
#         print(s)
#         if '00' not in s and '11' not in s:
#             k += 1
# print(k)

# k = 0
# for x in product('ВИШНЯ', repeat=6):
#     s = ''.join(x)
#     if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] not in 'ИЯ':
#         k += 1
#
# print(k)

# k = 0
# for x in product(sorted('ABCD'), repeat=4):
#     s = ''.join(x)
#     if s[0] <= s[1] <= s[2] <= s[3]:
#         k += 1
#         print(s)
# print(k)

# k = 0
# for x in product('ГЕПАРД', repeat=5):
#     s = ''.join(x)
#     if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
#         k += 1
#
# print(k)

# k = 0
# for x in product('0123456789', repeat=3):
#     s = ''.join(x)
#     if s[0] <= s[1] <= s[2] and s[0] != '0':
#         print(s)
#         k += 1
#
# print(k)

# k = 0
# for x in permutations('ДЕЙКСТРА', 6):
#     s = ''.join(x)
#     if s.count('Й') == 1:
#         for y in 'ДКСТР':
#             if 'Й' + y in s:
#                 k += 1
#
# print(k)


# k = 0
# for x in permutations('ВАЙФУ', 4):
#     s = ''.join(x)
#     if s[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
#         k += 1
# print(k)


# k = 0
# for x in set(permutations('МИМИКРИЯ', 8)):
#     s = ''.join(x)
#     k += 1
#     print(s)
# print(k)


# n = 0
# for x in product(sorted('ЛЕМУР'), repeat=4):
#     s = ''.join(x)
#     n += 1
#     if s[0] == 'Л':
#         print(n, s)
#         break

# n = 0
# for x in product(sorted('АЛГОРИТМ'), repeat=4):
#     s = ''.join(x)
#     n += 1
#     if s[-2] + s[-1] == 'ИМ':
#         print(n, s)


# n = 0
# for x in product(sorted('МАРИЯ'), repeat=4):
#     s = ''.join(x)
#     n += 1
#     if 'АРИЯ' in s:
#         print(n, s)

# n = 0
# for x in product(sorted('МАРИЯ'), repeat=4):
#     s = ''.join(x)
#     n += 1
#     if n == 211:
#         print(n, s)
