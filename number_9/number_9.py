# 2929

# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if (a[0] + a[2])/2 <= a[1]:
#         k += 1
# print(k)


# 4669

# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[3] + a[0] < a[1] + a[2]:
#         print(a)
#         k += 1
#
# print(k)


# 3150
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[2]**2 > 2*(a[0]*a[1]):
#         k += 1
#
# print(k)


# 3167
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if (a[0] + a[3])**2 > a[1]**2 + a[2]**2:
#         k += 1
# print(k)


# 4589
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[3] < a[0] + a[2] + a[3] and a[0] + a[3] == a[1] + a[2]:
#         k += 1
#
# print(k)


# 4633
# k = 0
#
# for s in open("09.txt"):
#     a = sorted([int(x) for x in s.split()])
#     if a[0] + a[3] == a[1] + a[2] and a[3] - a[0] < a[1] + a[2] - a[3]:
#         k += 1
# print(k)


# 4634
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[0] * a[3] == a[1] * a[2] and a[2]**2 > a[0] * a[3]:
#         k += 1
# print(k)


# 4636
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     if a[3] - a[0] >= 50 and a[1] * a[2] <= 1000:
#         k += 1
# print(k)


# 4637
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a10 = [n for n in a if n <= 10]
#     if a[3]**3 >= 2*(a[0] * a[1] * a[2]) and len(a10) == 0:
#         k += 1
# print(k)


# 4614
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) == 2]
#     if a[3] < a[0] + a[1] + a[2] and len(a2) == 2:
#         k += 1
# print(k)


# 5126
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a3 = [n for n in a if a.count(n) == 3]
#     a1 = [n for n in a if a.count(n) == 1]
#     if len(a3) == 3 and len(a1) == 3 and (a1[0] + a1[1] + a1[2])/3 <= a3[0] + a3[1] + a3[2]:
#         print(a1, a3)
#         k += 1
# print(k)


# 5284
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a3 = [n for n in a if a.count(n) == 3]
#     a1 = [n for n in a if a.count(n) == 1]
#     if len(a3) == 3 and len(a1) == 3 or (a[0] + a[5])**2 > a[1]**2 + a[2]**2 + a[3]**2 + a[4]**2:
#         k += 1
# print(k)


# 9740
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a3 = [n for n in a if a.count(n) == 3]
#     a1 = [n for n in a if a.count(n) == 1]
#     if len(a3) == 3 and len(a1) == 4 and (a1[0] + a1[1] + a1[2] + a1[3])/4 <= a3[0]:
#         k += 1
# print(k)


# 9778
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) == 2]
#     a1 = [n for n in a if a.count(n) == 1]
#     k += 1
#     if len(a2) == 2 and len(a1) == 4 and a2[0] >= (a1[0] + a1[1] + a1[2] + a1[3])/4:
#         print(a2, a1, k)


# 9832
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) == 2]
#     a1 = [n for n in a if a.count(n) == 1]
#     k += 1
#     if len(a1) == 3 and len(a2) == 4 and a[6] not in a2:
#         print(sum(a), k)


# 8609
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a1 = [n for n in a if a.count(n) > 1]
#     if len(a1) == 0 and 2*(a[0] + a[4]) <= 3*(a[1] + a[2] + a[3]):
#         k += 1
# print(k)


# 6357
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) > 1]
#     a1 = [n for n in a if a.count(n) == 1]
#     if len(a2) >= 1 and len(a1) >= 1 and sum(a1)/len(a1) < sum(a2)/len(a2):
#         k += 1
# print(k)


# 10910
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) > 1]
#     print(a2, a)
#     if a[0] not in a2 and (a[1] in a2 or a[2] in a2 or a[3] in a2 or a[4] in a2 or a[5] in a2) and a[0] + a[5] < sum(a2):
#         k += 1
# print(k)


# 6925
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a2 = [n for n in a if a.count(n) == 2]
#     a1 = [n for n in a if a.count(n) == 1]
#     aa = [n for n in a if n % 2 == 0]
#     aa1 = [n for n in a if n % 2 != 0]
#     try:
#         sr_aa = (sum(aa) / len(aa))
#     except ZeroDivisionError:
#         sr_aa = 0
#     try:
#         sr_aa1 = (sum(aa1) / len(aa1))
#     except ZeroDivisionError:
#         sr_aa1 = 0
#
#     if ((len(a2) == 2 and len(a1) == 4) + (sr_aa - sr_aa1 > 50 or sr_aa - sr_aa1 < -50)) == 1:
#         k += 1
# print(k)


# 6999
# k = 0
#
# for s in open('09.txt'):
#     a = sorted([int(x) for x in s.split()])
#     a_3 = [n for n in a if n % 3 == 0]
#     if len(a_3) == 3 and a[5] - a[0] <= sum(a_3):
#         k += 1
# print(k)


