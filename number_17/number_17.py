# 2003
#
# a = [int(x) for x in open('17_2003.txt')]
#
# aws = []
#
# for i in range(len(a)):
#     if a[i] % 3 == 0 and a[i] % 7 != 0 and a[i] % 17 != 0 and a[i] % 19 != 0 and a[i] % 27 != 0:
#         aws.append(a[i])
#
# print(len(aws), max(aws))


# 2013

# a = [int(x) for x in open('17_2013.txt')]
#
# aws = []
# for i in range(len(a)):
#     if (a[i] % 10 == 2 or a[i] % 10 == 7) and a[i] % 3 == 0 and a[i] % 11 == 0:
#         aws.append(a[i])
#
# print(len(aws), min(aws))


# 2015

# a = [int(x) for x in open('17_2015.txt')]
#
# aws = []
#
# for i in range(len(a)):
#     if (a[i] % 10 == 5 or a[i] % 10 == 7) and a[i] % 9 != 0 and a[i] % 11 != 0:
#         aws.append(a[i])
#
# print(len(aws), max(aws) + min(aws))


# 2016

# a = [int(x) for x in open('17_2016.txt')]
#
# ans = []
#
# for i in range(len(a)):
#     if a[i] % 13 == 7 and a[i] % 7 != 0 and a[i] % 11 != 0:
#         ans.append(a[i])
#
# print(max(ans) - min(ans), len(ans))


# 2017

# a = [int(x) for x in open('17_2017.txt')]
#
# ans = []
#
# for i in range(len(a)):
#     if a[i] % 16 == 11 and a[i] % 7 == 0 and a[i] % 6 != 0 and a[i] % 13 != 0 and a[i] % 19 != 0:
#         ans.append(a[i])
#
# print(sum(ans), len(ans))


# 1993

# a = [int(x) for x in open('17_1993.txt')]
#
# ans = []
# for i in range(len(a)-1):
#     if abs(a[i] + a[i+1]) % 3 == 0 and abs(a[i] + a[i+1]) % 6 != 0 and abs(a[i] * a[i+1]) % 10 == 8:
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), max(ans))


# 1994

# a = [int(x) for x in open('17_1994.txt')]
#
# ans = []
#
# for i in range(len(a) - 1):
#     if (a[i] * a[i+1]) > 0 and (a[i] + a[i+1]) % 7 == 0:
#         ans.append(a[i] * a[i+1])
#
# print(len(ans), min(ans))


# 1998

# a = [int(x) for x in open('17_1998.txt')]
#
# ans = []
#
# for i in range(len(a) - 2):
#     if (a[i] * a[i+1] * a[i+2]) % 7 == 0 and (a[i] + a[i+1] + a[i+2]) % 10 == 5:
#         ans.append(a[i] + a[i+1] + a[i+2])
#
# print(len(ans), max(ans))


# 1999

# a = [int(x) for x in open('17_1999.txt')]
#
# ans = []
#
# for i in range(len(a) - 2):
#     if (a[i] % 12 == 0) + (a[i+1] % 12 == 0) + (a[i+2] % 12 == 0) >= 1 and abs(a[i]) % 3 == 0 and abs(a[i+1]) % 3 == 0 and abs(a[i+2]) % 3 == 0:
#         ans.append((a[i] + a[i+1] + a[i+2])//3)
#
# print(len(ans), min(ans))


# 2402

# a = [int(x) for x in open('17_2402.txt')]
#
# ans = []
#
# for i in range(len(a) - 2):
#     if a[i] % 3 == 2 or a[i+1] % 3 == 2 or a[i+2] % 3 == 2:
#         ans.append(min(a[i], a[i+1], a[i+2]))
#
# print(len(ans), sum(ans))


# 2002

# a = [int(x) for x in open('17_2002.txt')]
#
# ans = []
#
# for i in range(len(a) - 3):
#     if a[i] > a[i+1] > a[i+2] > a[i+3] and max(a[i], a[i+1], a[i+2], a[i+3]) - min(a[i], a[i+1], a[i+2], a[i+3]) > 1000:
#         ans.append(a[i] + a[i+1] + a[i+2] + a[i+3])
#
# print(len(ans), min(ans))


# 2400

# a = [int(x) for x in open('17_2400.txt')]
#
# ans = []
#
# for i in range(len(a)-1):
#     if a[i] + a[i+1] >= 100 and (a[i] < 0 or a[i+1] < 0):
#         ans.append(a[i] * a[i+1])
#
# print(len(ans), max(ans))


# 2401

# a = [int(x) for x in open('17_2401.txt')]
#
# ans = []
#
# for i in range(len(a)-1):
#     if 50 <= abs(a[i]) + abs(a[i+1]) <= 200:
#         ans.append(min(a[i], a[i+1]))
#
# print(len(ans), min(ans))


# 2238

# a = [int(x) for x in open('17_2238.txt')]
#
# ans = []
# avr = sum(a)/len(a)
#
# for i in range(len(a)-2):
#     if (a[i] > avr) + (a[i+1] > avr) + (a[i+2] > avr) >= 2:
#         ans.append(a[i] + a[i+1] + a[i+2])
#
# print(len(ans), max(ans))


# 2239
#
# a = [int(x) for x in open('17_2239.txt')]
#
# a_max_19 = max([x for x in a if x % 19 == 0])
#
# ans = []
#
# for i in range(len(a)-1):
#     if a[i] > a_max_19 or a[i+1] > a_max_19:
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), min(ans))


# 2309

# a = [int(x) for x in open('17_2309.txt')]
#
# ans = []
#
# a11 = [x for x in a if x % 11 == 0]
# a17 = [x for x in a if x % 17 == 0]
#
# if len(a11) > len(a17):
#     print(len(a11), min(a11))
# else:
#     print(len(a17), max(a17))


# 2310
#
# a = [int(x) for x in open('17_2310.txt')]
#
# ans = []
#
# a_4 = [x for x in a if x % 10 == 4]
#
# for i in range(len(a)-1):
#     if (a[i] + a[i+1]) < (max(a_4) + min(a_4)):
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), max(ans))


# 2403

# a = [int(x) for x in open('17_2403.txt')]
#
# ans = []
#
# for i in range(len(a)-1):
#     if (a[i] % 9 == 0 and a[i+1] % 9 != 0 and a[i+1] % 8 == 3) or (a[i+1] % 9 == 0 and a[i] % 9 != 0 and a[i] % 8 == 3):
#         ans.append(max(a[i], a[i+1]))
#
# print(len(ans), max(ans))


# 2398
#
# a = [int(x) for x in open('17_2398.txt')]
#
# ans = []
#
# for i in range(len(a) - 2):
#     if (a[i+1] > 0 and abs(a[i+1] % 10) == 9) and (a[i] <= 0 or abs(a[i]) % 10 != 9) and (a[i+2] <= 0 or abs(a[i+2]) % 10 != 9):
#         ans.append(a[i] + a[i+1] + a[i+2])
#
# print(len(ans), max(ans))


# 2399

# a = [int(x) for x in open('17_2399.txt')]
#
# ans = []
# a_35 = [int(x) for x in a if x % 35 == 0 for x in str(x)]
#
# for i in range(len(a)-1):
#     if (a[i] > sum(a_35) and a[i+1] <= sum(a_35) and a[i+1] // 16 % 16 == 14 and  a[i+1] % 16 == 15) or (a[i+1] > sum(a_35) and a[i] <= sum(a_35) and a[i] // 16 % 16 == 14 and  a[i] % 16 == 15): # 0 1 2 3 4 5 6 7 8 9 A B C D E F
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), min(ans))



