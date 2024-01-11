# print('w x y z F')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = (not(x <= y)) or (x == z) or w
#                 if F == 0:
#                     print(w, x, y, z, F)

# for N in range(12, 50):
#     a = N % 4
#     b = N // 4
#     quaternary = str(b % 4) + str(a)
#     if N % 4 == 0:
#         new_quaternary = quaternary + quaternary[-2] + quaternary[-1]
#     if N % 4 != 0:
#         ostatok = (int(quaternary) % 4) * 2
#         a = ostatok % 4
#         b = ostatok // 4
#         ost_quaternary = str(b % 4) + str(a)
#         new_quaternary = quaternary + str(ost_quaternary)
#     dec = int(new_quaternary[0]) * 4**3 + int(new_quaternary[1]) * 4**2 + int(new_quaternary[2]) * 4**1 + int(new_quaternary[3]) * 4**0
#     if dec < 261:
#         print('Исходное число N:', N)
#         print('Результат:', dec)
#         print("------------------------")


# for N in range(16, 17):
#     a = N % 4
#     b = N // 4
#     quaternary = str(b % 4) + str(a)
#     if N % 4 == 0:
#         new_quaternary = quaternary + quaternary[-2] + quaternary[-1]
#     if N % 4 != 0:
#         ostatok = (int(quaternary) % 4) * 2
#         a = ostatok % 4
#         b = ostatok // 4
#         ost_quaternary = str(b % 4) + str(a)
#         new_quaternary = quaternary + str(ost_quaternary)
#     # dec = int(new_quaternary[0]) * 4**3 + int(new_quaternary[1]) * 4**2 + int(new_quaternary[2]) * 4**1 + int(new_quaternary[3]) * 4**0
#     # print(dec)
#     # if dec < 261:
#     print('Исходное число N:', N)
#     print('Результат:', new_quaternary)
#     print("------------------------")

# a = 6 % 4
# b = 6 // 4
# quaternary = str(b % 4) + str(a)
# print(quaternary)

# for x in range(23):
#     a = 1*23**8 + x*23**7 + 1*23**6 + x*23**5 + 1*23**4 + x*23**3 + 1*23**2 + x*23**1 + 1*23**0
#     b = 2*23**4 + 0*23**3 + x*23**2 + 2*23**1 + 4
#     c = 1*23**4 + x*23**3 + 2*23**2 + 3*23**1 + 5
#     if (a+b+c) % 22 == 0:
#         result = (a+b+c) // 22
#         print(result)

# print('w x y z F')
#
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = y and (x <= w) and ((not(x)) <= ((not(w)) == z))
#                 print(w, x, y, z, bool(F))


"""
w x y z F
0 0 1 1 True
1 0 1 0 True
0 1 1 1 False

x z y w F
0 1 1 0
0 0 1 1
1 1 1 0

"""
# i = 3
# for i in range(1, 50):
#     number_bin = bin(i)[2:]
#     if i % 2 == 0:
#         number_bin = number_bin + '0'
#     else:
#         number_bin = number_bin + '1'
#     if sum(map(int, number_bin)) % 3 == 0:
#         number_bin = number_bin.replace(number_bin[:2], '11')
#     else:
#         number_bin = number_bin.replace(number_bin[:2], '10')
#     if int(number_bin, 2) < 37:
#         print(i)
# print(int(number_bin, 2), number_bin)

# s = '22' + 2050 * '1' + '22'
# while '211' in s or '112' in s:
#     s = s.replace('11', '1', 1)
#     if '21' in s:
#         s = s.replace('21', '12', 1)
#     else:
#         s = s.replace('12', '1', 1)
# print(s)

# s = 4 ** 2022 - 6 * 4 ** 522 + 5 * 64 ** 510 - 3 * 2 ** 330 - 100
# a = []
# while s > 8:
#     a = [s % 8] + a
#     s = s // 8
# print(a)
# print(a.count(7))


# print('w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = ((z <= y) <= x) or (not(w))
#                 if F == 0:
#                     print(w, x, y, z, bool(F))

# n = input()
# for n in range(621, 1000):
#     n = str(n)
#     n1 = int(n[0])**2 + int(n[1])**2
#     n2 = int(n[1])**2 + int(n[2])**2
#     if n1 > n2:
#         n3 = str(n1) + str(n2)
#     else:
#         n3 = str(n2) + str(n1)
#     if n3 == '7434':
#         print(n)

# from itertools import *
#
# k = 0
# for x in product(sorted('ПРАВО'), repeat=4):
#     s = ''.join(x)
#     k += 1
#     if s[0] == 'П':
#         print(k, s)
#         break

# s = '1' * 2022
#
# while '11' in s or '555' in s:
#     if '11' in s:
#         s = s.replace('11', '555', 1)
#     else:
#         s = s.replace('555', '5', 1)
#
# print(s)
#
# s = 4 ** 2022 - 2*4**1111 + 16**600 + 192
# a = []
#
# while s > 4:
#     a = [s % 4] + a
#     s = s // 4
# print(a.count(3))

# print('w x y z F')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 F = x and (y <= z) and ((not(y)) <= ((not(z)) == w))
#                 print(w, x, y, z, bool(F))


# for n in range(1, 100):
#     bin_n = bin(n)[2:]
#     if n % 2 == 0:
#         bin_n = str(bin_n) + '0'
#     else:
#         bin_n = str(bin_n) + '1'
#
#     count_1 = bin_n.count('1')
#     if count_1 % 3 == 0:
#         bin_n = '11' + str(bin_n[2:])
#     else:
#         bin_n = '10' + str(bin_n[2:])
#
#     dec = int(bin_n, 2)
#
#     if dec >= 26:
#         print('N', n)
#         break

# s = '22' + '1'*2023 + '22'
#
# while '211' in s or '112' in s:
#     s = s.replace('11', '1', 1)
#     if '21' in s:
#         s = s.replace('21', '12', 1)
#     else:
#         s = s.replace('12', '1', 1)
#
# print(s)

# s = 4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3 * 5**100 - 660
# a = []
# while s > 5:
#     a = [s % 5] + a
#     s = s // 5
#
# print(a.count(4))


# for n in range(10, 101):
#     bin_n = bin(n)[2:]
#     if n % 2 == 0:
#         new_n = str(bin_n) + str(bin_n)[-2] + str(bin_n)[-1]
#     elif n % 2 != 0:
#         new_n = '1' + str(bin_n) + '0'
#     result = int(new_n, 2)
#     if result < 100:
#         print(n, result)


# print((1280*1024*10*220)/12582912)

# from itertools import *
# k = 0
# for x in product('012345678', repeat=5):
#     n = ''.join(x)
#     if n[0] != '0':
#         if n.count('5') == 1:
#             if n[0] != n[1] != n[2] != n[3] != n[4]:
#                 k += 1
# print(k)


# print((110*11*32768)/(8*1024))
# print((110*11)/8)
# print((152*32768)/1024)
# a = []
# for n in range(4, 10000):
#     s = '3' + n * '5'
#     while '333' in s or '555' in s:
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#         else:
#             s = s.replace('333', '5', 1)
#     a.append(sum(map(int, s)))
#     print(n)
# print(max(a))


# t = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
# a = []
# res = []
# while t > 0:
#     a = [t % 9] + a
#     t //= 9
# for i in a:
#     if i != 0:
#         res.append(i)
# print(len(res))


# from itertools import *
#
# for s in product('0123456789ABCDEF', repeat=4):
#     x = ''.join(s)
#     if x[0] != '0':
#         for a in x:
#             if a == 'A':
#                 x.replace(a, '10')
#                 print(x)
        #         if int(a) % 2 == 0:
        #             x.replace(a, '0')
        #         if int(a) % 2 != 0:
        #             x.replace(a, '1')
        # print(x)


# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'174.213.57.95/{mask}', 0)
#     print(net)


# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'134.181.67.112/{mask}', 0)
#     net1 = ip_network(f'134.181.94.117/{mask}', 0)
#     if net == net1:
#         print(net, net.netmask)
# print(255+224)


# from ipaddress import *
#
# k = 0
#
# net = ip_network('123.222.99.192/255.255.255.248', 0)
# for n in net:
#     bin_n = f'{n:b}'
#     if bin_n.count('1') > bin_n.count('0'):
#         k += 1
# print(k)


# from ipaddress import *
#
# k = 0
#
# net = ip_network('128.224.31.192/255.255.255.192', 0)
# for n in net:
#     bin_n = f'{n:b}'
#     if bin_n.count('0') / 16 == 1:
#         k += 1
# print(k)


# def f(x):
#     return (x&a != 0) <= ((x&17 == 0 and x&5 == 0) <= (x&3 != 0))
#
# for a in range(1000):
#     if all(f(x) for x in range(100000)):
#         print(a)


# from itertools import *
#
#
# def f(x):
#     P = 13 <= x <= 19
#     Q = 17 <= x <= 23
#     A = a1 <= x <= a2
#     return (not((not P) <= Q)) <= (A <= (not Q) <= P)
#
#
# Ox = [i/4 for i in range(12*4, 24*4)]
# m = []
#
# for a1, a2 in combinations(Ox, 2):
#     print(a1, a2)
#     if all(f(x) for x in range(1000)):
#         m.append(a2 - a1)
#
# print(m)

from itertools import *

# def f(x):
#     B = 15 <= x <= 40
#     C = 21 <= x <= 63
#     A = a1 <= x <= a2
#     b = x in B
#     c = x in C
#     a = x in A
#     return (not(B)) <= ((C and (not (A))) <= B)
#
#
# Ox = [i/4 for i in range(14*4, 64*4)]
# m = []
#
#
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) for x in Ox):
#         m.append(a2-a1)
# print(min(m))


# def f(x, y):
#     return (3*x + 4*y != 101) or (x < a) or (3*y <= a)
#
#
# for a in range(1, 1000):
#     if all(f(x, y) for x in range(1, 10000) for y in range(1, 10000)):
#         print(a)


# from itertools import *
#
# k = 0
# for x in permutations('КОБУРА'):
#     s = ''.join(x)
#     s = s.replace('О', '1').replace('У', '1').replace('А', '1')
#     s = s.replace('К', '0').replace('Б', '0').replace('Р', '0')
#     if s[0] != s[1] != s[2] != s[3] != s[4] != s[5]:
#         k += 1
# print(k)

# k = 0
# for x in permutations('0123456789', r=5):
#     s = ''.join(x)
#     if s[0] != '0' and '5' not in s:
#         for i in range(5):
#             if int(s[i]) % 2 == 0:
#                 s = s.replace(s[i], '0')
#             else:
#                 s = s.replace(s[i], '1')
#         if s[0] != s[1] != s[2] != s[3] != s[4]:
#             # print(s)
#             k += 1
# print(k)

