# 11

# s = 70 * '8'
#
# while '2222' in s or '8888' in s:
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
#
# print(s)


# 56

# s = '2' + '5' * 81
#
# while '25' in s or '355' in s or '4555' in s:
#     if '25' in s:
#         s = s.replace('25', '4', 1)
#     if '355' in s:
#         s = s.replace('355', '2', 1)
#     if '4555' in s:
#         s = s.replace('4555', '3', 1)
#
# print(s)


# 375

# s = '1' + 33 * '0'
#
# while '1' in s or '100' in s:
#     if '100' in s:
#         s = s.replace('100', '0001', 1)
#     else:
#         s = s.replace('1', '00', 1)
#
# print(s.count('0'))


# 645
#
# s = 46 * '1' + 31 * '2'
#
# while '1111' in s:
#     s = s.replace('1111', '2', 1)
#     s = s.replace('222', '1', 1)
#
# print(s)


# 648

# for i in range(51):
#     s = i * '6'
#     while '66' in s:
#         s = s.replace('66', '1', 1)
#         s = s.replace('11', '2', 1)
#         s = s.replace('22', '6', 1)
#     if s == '21':
#         print(i, s)


# 649

# s = '>' + 11 * '1' + 12 * '2' + 30 * '3'
#
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>')
#     if '>2' in s:
#         s = s.replace('>2', '2>')
#     if '>3' in s:
#         s = s.replace('>3', '1>')
# print(sum([int(x) for x in s[:-1]]))


# 1118

# for x in range(50):
#     for y in range(50):
#         for z in range(50):
#             s = '0' + x * '1' + y * '2' + z * '3'
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01', '302', 1)
#                 s = s.replace('02', '3103', 1)
#                 s = s.replace('03', '20', 1)
#             if s.count('1') == 28 and s.count('2') == 34 and s.count('3') == 45:
#                 print(x, s)


# 1261
#
# s = '1121121121121111'
#
# while '11' in s:
#     if '112' in s:
#         s = s.replace('112', '7', 1)
#     else:
#         s = s.replace('11', '3', 1)
#
# print(sum([int(x) for x in s]))


# 1411

# s = 33 * '9992' + '9' + 14 * '1' + '2' * 15
# while '999' in s or '22' in s:
#     if '999' in s:
#         s = s.replace('999', '12', 1)
#     else:
#         s = s.replace('22', '1', 1)
# print(s.count('1'))


# 2229
# m = set()
# for x in range(1, 100):
#     s = '5' * x
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55', 1)
#     m.add(s)
# print(len(m))


# 2223

# a = 'КАРА'
#
# i = len(a)
# k = 1
# b = 'Т'
# while i > 1:
#     c = a[i-1]
#     b = b + c
#     i = i - 1
# print(b)


# 2224
a = 'ИНФОРМАТИКА'
m = 10
b = a[m-1]
for k in range(4, 6):
    c = a[k-1]
    b = b + c
for k in range(1, 4):
    c = a[k-1]
    b = b + c
print(b)