# 49

# for n in range(1, 100):
#     b = bin(n)[2:]
#     del_sum_b = sum(map(int, b))
#     b = b + str(del_sum_b % 2)
#     del_sum_b = sum(map(int, b))
#     b = b + str(del_sum_b % 2)
#     number = int(b, 2)
#     print(n, number)


# 405

# for n in range(1, 100):
#     bin_n = bin(n)[2:]
#     if n % 2 == 0:
#         bin_n = bin_n + '01'
#     else:
#         bin_n = bin_n + '10'
#     number = int(bin_n, 2)
#     print(number)


# 549

# for n in range(1, 100):
#     b = bin(n)[2:]
#     b += b[-1]
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     number = int(b, 2)
#     print(n, number)


# 557

# for n in range(1, 100):
#     b = bin(n)[2:]
#     b += b[-1]
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     number = int(b, 2)
#     print(number)


# 561

# def cc3(x):
#     a = []
#     t = x
#     while t > 0:
#         a = [t % 3] + a
#         t //= 3
#     return a
#
#
# for n in range(1, 100):
#     n3 = cc3(n)
#     n3.append(n % 3)
#     n3_list_str = [str(x) for x in n3]
#     n3_str = ''.join(n3_list_str)
#     number = int(n3_str, 3)
#     print(n, number)


# 563

# for n in range(1, 101):
#     bin_n = bin(n)[2:]
#     bin_n_rev = bin_n[::-1]
#     if bin_n_rev[0] == '0':
#         bin_n_rev = bin_n_rev.lstrip('0')
#     number = int(bin_n_rev, 2)
#     if number == 13:
#         print(n, number)


# 553

# k = 0
# for n in range(1, 100):
#     bin_n = bin(n)[2:]
#     bin_n += str(sum(map(int, bin_n)) % 2)
#     bin_n += str(sum(map(int, bin_n)) % 2)
#     number = int(bin_n, 2)
#     if number < 80:
#         k += 1
#         print(n, number)
# print(k)


# 1732

# for n in range(1, 1000):
#     bin_2n = bin(2*n)[2:]
#     bin_2n += str(sum(map(int, bin_2n)) % 2)
#     bin_2n += str(sum(map(int, bin_2n)) % 2)
#     number = int(bin_2n, 2)
#     if number > 1017:
#         print(n, number)


# 1849

# a = []
# for n in range(1, 100):
#     bin_n = bin(n)[2:]
#     if n % 2 == 0:
#         bin_n = '1' + bin_n + '0'
#     else:
#         bin_n = '11' + bin_n + '11'
#     number = int(bin_n, 2)
#     if number > 52:
#         print(n, number)
#         a.append(number)
# print(min(a))


# 4610
#
# for n in range(1, 1000):
#     bin_n = bin(n)[2:]
#     if sum(map(int, bin_n)) % 2 == 0:
#         bin_n = '10' + bin_n[2:] + '0'
#     else:
#         bin_n = '11' + bin_n[2:] + '1'
#     number = int(bin_n, 2)
#     if number < 35:
#         print(n, number)


# 9828

# def cc3(x):
#     a = []
#     t = x
#     while t > 0:
#         a = [t % 3] + a
#         t //= 3
#     return a
#
#
# for n in range(1, 100):
#     n3 = cc3(n)
#     if n % 3 == 0:
#         n3 = [1] + n3 + [0] + [2]
#     else:
#         ost = (n % 3) * 4
#         n3_ost = cc3(ost)
#         n3 = n3 + n3_ost
#     n3_str = [str(x) for x in n3]
#     dec_n = int(''.join(n3_str), 3)
#     if dec_n < 199:
#         print(n, dec_n)


# 10707

# def cc6(x):
#     a = []
#     t = x
#     while t > 0:
#         a = [t % 6] + a
#         t //= 6
#     return a
#
#
# for n in range(10, 100):
#     n6 = cc6(n)
#     if n % 3 == 0:
#         n6 = n6 + [n6[0]] + [n6[1]]
#     else:
#         n6 = n6 + cc6((n % 3) * 10)
#     n6_str = [str(x) for x in n6]
#     n6_str = int(''.join(n6_str), 6)
#     if n6_str > 680:
#         print(n, n6_str)


# 4869

# for n in range(2, 10000):
#     bin_n = bin(n)[2:]
#     a_1 = 0
#     a_0 = 0
#     for i in range(1, len(str(bin_n).lstrip('0')) + 1):
#         if i % 2 == 0:
#             if bin_n[i-1] == '1':
#                 a_1 += 1
#                 # print(bin_n, i, bin_n[i-1])
#         else:
#             if bin_n[i-1] == '0':
#                 a_0 += 1
#                 # print(bin_n, i, bin_n[i-1])
#     if abs(a_1 - a_0) == 5:
#         print(n, abs(a_1 - a_0))


# 971

# for n in range(1000, 10000):
#     str_n = str(n)
#     a1 = int(str_n[0]) * int(str_n[1])
#     a2 = int(str_n[2]) * int(str_n[3])
#     if a1 < a2:
#         r = str(a1) + str(a2)
#     else:
#         r = str(a2) + str(a1)
#     if r == '1214':
#         print(n, r)


# 972

# for n in range(100, 1000):
#     str_n = str(n)
#     a1 = int(str_n[0]) * int(str_n[1])
#     a2 = int(str_n[1]) * int(str_n[2])
#     if a1 > a2:
#         r = str(a1) + str(a2)
#     else:
#         r = str(a2) + str(a1)
#     if r == '240':
#         print(n, r)


# 2461

# for n in range(100, 1000):
#     str_n = str(n)
#     a1 = (int(str_n[0]))**2 + (int(str_n[1]))**2
#     a2 = (int(str_n[1])) ** 2 + (int(str_n[2])) ** 2
#     if a1 > a2:
#         r = str(a1) + str(a2)
#     else:
#         r = str(a2) + str(a1)
#     if r == '9010':
#         print(n, r)


# 3073

# for n in range(100, 1000):
#     str_n = str(n)
#     a_str = [str_n[0] + str_n[1], str_n[0] + str_n[2], str_n[1] + str_n[0], str_n[1] + str_n[2], str_n[2] + str_n[1], str_n[2] + str_n[0]]
#     a_str_not_0 = [int(x) for x in a_str if x[0] != '0']
#
#     if int(max(a_str_not_0)) - int(min(a_str_not_0)) == 5:
#         print(n, int(max(a_str_not_0)) - int(min(a_str_not_0)))


# 4870

# for m in range(1, 1000):
#     p1 = p2 = 1
#     d = [int(c) for c in str(m)]
#     for c in d:
#         if c % 2 == 0 and c > 0:
#             p1 *= c
#         else:
#             p2 *= c
#     p1 *= 2
#     r = abs(p2 - p1)
#     if r == 29:
#         print(m)


# 4870

# k = 0
# for n in range(300, 401):
#     n_str = str(n)
#     a = [n_str[0] + n_str[1], n_str[0] + n_str[2], n_str[1] + n_str[0], n_str[1] + n_str[2], n_str[2] + n_str[0], n_str[2] + n_str[1]]
#     a1 = [int(x) for x in a if x[0] != '0']
#     r = max(a1) - min(a1)
#     if r == 20:
#         print(n, r)
#         k += 1
# print(k)


# 3755

# for n in range(100, 1000):
#     n_str = str(n)
#     a = [n_str[0] + n_str[1], n_str[1] + n_str[2]]
#     r = int(max(a)) - int(min(a))
#     if r == 44:
#         print(n, r)


# 4867

# for n in range(2, 10000):
#     a = sum([int(x) for x in str(n) if int(x) % 2 == 0])
#     a1 = []
#     for i in range(1, len(str(n)) + 1):
#         if i % 2 == 0:
#             a1.append(int(str(n)[i-1]))
#     r = abs(a - sum(a1))
#     if r == 9:
#         print(n, r)


# 4871

# k = 0
#
# for n in range(2, 1000000):
#     x = n
#     if x % 3 == 0:
#         x //= 3
#     else:
#         x -= 1
#     if x % 5 == 0:
#         x //= 5
#     else:
#         x -= 1
#     if x % 11 == 0:
#         x //= 11
#     else:
#         x -= 1
#     if x == 8:
#         k += 1
#         print(n, x)
# print(k)























