# 12462

# from itertools import *
#
# k = 0
# for i in product('0123456789ABCDEF', repeat=3):
#     s = ''.join(i)
#     if s[0] != '0':
#         if s[0] > s[1] > s[2]:
#             k += 1
#
#
# for i in product('0123456789ABCDEF', repeat=5):
#     s = ''.join(i)
#     if s[0] != '0':
#         if s[0] > s[1] > s[2] > s[3] > s[4]:
#             k += 1
#
# print(k)


# 12240

# from itertools import *
#
#
# k = 0
# for i in product('012345678', repeat=5):
#     s = ''.join(i)
#     if s[0] != '0' and s.count('5') == 1:
#         if s[0] != s[1] != s[2] != s[3] != s[4]:
#             k += 1
# print(k)


# 12097

# from itertools import *
#
# k = 0
#
# for i in sorted(product('ГИРЛЯНДА', repeat=6)):
#     s = ''.join(i)
#     k += 1
#     if k % 2 == 0 and s[0] != 'Я' and s.count('Д') == 3:
#         print(k, s)

