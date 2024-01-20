# 2419

# s = open('24_2419.txt').readline()
# s = s.replace('A', ' ').replace('B', ' ')
# print(max(len(x) for x in s.split(' ')))


# 2420

# s = open('24_2420.txt').readline()
# s = s.replace('C', ' ').replace('D', ' ')
# print(max(len(x) for x in s.split(' ')))


# 2421

# s = open('24_2421.txt').readline()
# s = s.replace('D', ' ')
# print(max(len(x) for x in s.split(' ')))


# 865

# s = open('24_865.txt').readline()
# s = s.replace('C', ' ').replace('F', ' ')
# print(max(len(x) for x in s.split(' ')))


# 2426

# s = open('24_2426.txt').readline()
# s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
# print(max(len(x) for x in s.split(' ')))


# 1040

# s = open('24_1040.txt').readline()
# k = m = 0
#
# for i in range(len(s)):
#     if s[i] in '1234567890':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
#
# print(m)


# 1428

# s = open('24_1428.txt').readline()
# k = m = 1
#
# for i in range(len(s)-1):
#     if s[i] + s[i+1] != 'XY' and s[i] + s[i+1] != 'XZ' :
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# 1975
#
# s = open('24_1975.txt').readline()
# while 'PP' in s:
#     s = s.replace('PP', 'P P')
# print(max([len(x) for x in s.split(' ')]))


# 1302

# s = open('24_1302.txt').readline()
# s = s.replace('XZZY', 'XZZ ZZY')
# print(max(len(x) for x in s.split(' ')))


# 21

# s = open('24_21.txt').readline()
#
# k = m = 1
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# 2422

# s = open('24_2422.txt').readline()
#
# k = m = 1
# for i in range(len(s)-1):
#     if s[i] <= s[i+1]:
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# 2423

# s = open('24_2423.txt').readline()
#
# k = m = 1
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# 2427

# s = open('24_2427.txt').readline()
#
# k = m = 1
# char = ''
# for i in range(len(s)-1):
#     if s[i] > s[i+1]:
#         k += 1
#         m = max(m, k)
#         char += s[i]
#     else:
#         k = 1
#         char = ''
#     print(char)


# 1145

# s = open('24_1145.txt').readline()
#
# m = 10000
#
# for i in s.split('D')[1:-1]:
#     if i != '':
#         m = min(m, len(i) + 2)
# print(m)


# 1146

# s = open('24_1146.txt').readline()
# m = 10000
# sub = ''
#
# for i in range(len(s)):
#     if s[i] == 'D':
#         sub += s[i]
#     elif sub != '':
#         m = min(m, len(sub))
#         sub = ''
# print(m)


# 2250

# s = open('24_2250.txt').readline()
# s = s.split('A')
#
# m = 0
# for i in range(len(s)-1):
#     x = s[i] + 'A' + s[i+1]
#     m = max(m, len(x))
# print(m)


# 2251

# s = open('24_2251.txt').readline()
# s = s.split('D')
#
# m = 0
# for i in range(len(s)-2):
#     sub = s[i] + 'D' + s[i+1] + 'D' + s[i+2]
#     m = max(len(sub), m)
# print(m)


# 66

# s = open('24_66.txt').readline()
#
# s = s.replace('KOT', '*')
# s = s.replace('K', ' ').replace('O', ' ').replace('T', ' ')
#
# print(max(len(x) for x in s.split(' ')))


# 4602

# s = open('24_4602.txt').readline()
# s = s.replace('BA', '*').replace('CA', '*').replace('DA', '*').replace('CO', '*').replace('DO', '*').replace('BO', '*')
# k = m = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
# print(m)


# 4642

# s = open('24_4642.txt').readline()
# s = s.replace('A1', '*').replace('B1', '*').replace('A2', '*').replace('B2', '*')
# k = m = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         k += 1
#         m = max(k, m)
#     else:
#         k = 0
# print(m)


# 4627
#
# s = open('24_4627.txt').readline()
# s = s.replace('PNO', '*').replace('NPO', '*')
# s = s.replace('N', ' ').replace('O', ' ').replace('P', ' ')
#
# print(max(len(x) for x in s.split(' ')))
# # PNO + NPO = 327
# # PNO = 22
# # NPO = 18


# 4643

# s = open('24_4643.txt').readline()
# s = s.replace('B', 'A').replace('2', '1')
# s = s.replace('11A', '*').replace('A', ' ').replace('1', ' ')
# print(max(len(x) for x in s.split(' ')))


# 4546

# s = open('24_4546.txt').readline()
#
# m = 0
# for x in range(3):
#     k = 0
#     for i in range(x, len(s)-2, 3):
#         if s[i] + s[i+2] == 'AA' or s[i] + s[i+2] == 'CC':
#             k += 1
#             m = max(m, k)
#         else:
#             k = 0
# print(m)


# 5171
#
# s = open('24_5171.txt').readline()
#
# c = ''
# while c in s:
#     c += 'CA'
#
# c = c[:-2]
# print(c in s)
# print(len(c))


# 2425
# s = open('24_2425.txt').readline()
#
# c = ''
# while c in s:
#     c += 'DBAC'
#
# c = c[:-1]
# print(len(c))
# print(c in s)













