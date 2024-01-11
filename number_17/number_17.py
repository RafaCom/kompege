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





